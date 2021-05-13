N, M = map(int, input().split())
S = input()
S = S[::-1]
now = 0
ans = []

while now<N:
    for i in range(M, 0, -1):
        if now+i>N:
            continue
    
        if S[now+i]=='0':
            ans.append(i)
            now += i
            break
    else:
        print(-1)
        exit()

print(*ans[::-1])