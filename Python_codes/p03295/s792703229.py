def main():
    N, M = map(int, input().split())
    y = []
    for i in range(M):
        y.append(list(map(int, input().split())))
    youbou = sorted(y, key = lambda x:x[1])
    
    cnt = 0
    k = 0
    for i in range(M):
        if(youbou[i][0] >= k):
            cnt += 1
            k = youbou[i][1]
    print(cnt)
main()