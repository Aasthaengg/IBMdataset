n=int(input())
A = list(map(int,input().split()))

amul=1
for i in range(n):
    amul *= A[i]
asum=0
for i in range(n):
    asum += amul//A[i]

ans = amul / asum
print(ans)