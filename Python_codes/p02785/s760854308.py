N,K=map(int, input().split())
H=list(map(int, input().split()))

H=sorted(H)[::-1]

for i in range(min(N,K)):
    H[i] = 0

ans =sum(H)
print(ans)