def main():
    N, M = map(int, input().split())
    island = []
    for i in range(M):
        a, b = map(int, input().split())
        island.append(tuple((a, b)))
    
    s = sorted(island, key=lambda x:x[1])
    
    base = s[0][1]
    cnt = 1
    for i in range(1, len(s)):
        if(s[i][0] >= base):
            base = s[i][1]
            cnt += 1
    print(cnt)
    
main()