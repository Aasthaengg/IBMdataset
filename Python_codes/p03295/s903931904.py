def main():
    N, M = map(int, input().split())
    wish = []
    for i in range(M):
        wish.append(tuple(map(int, input().split())))
    w = sorted(wish, key=lambda x:x[1])
    
    cnt = 0
    ans = 0
    for i in range(M):
        if(w[i][0] >= cnt):
            ans += 1
            cnt = w[i][1]
    print(ans)
main()