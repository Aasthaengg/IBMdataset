N,X = map(int,input().split())
M = sorted([int(input()) for i in range(N)])
ans = N

X -= sum(M)
ans += X//M[0]

print(ans)