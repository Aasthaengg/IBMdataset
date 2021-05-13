N,M = map(int,input().split())
S = input()[::-1]
ans = []
cur = 0
while cur < N:
    for i in range(1,min(M+1,N-cur+1))[::-1]:
        if S[cur+i] == '0':
            ans.append(i)
            cur += i
            break
    else:
        print(-1)
        exit()
print(*ans[::-1])