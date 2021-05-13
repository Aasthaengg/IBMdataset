#平均値に近づけるという考え方が間違い-->中央値に近づける

N = int(input())
A = list(map(int, input().split()))

A = [A[i]-(i+1) for i in range(N)]

A.sort()

center1 = A[N//2]
if N == 1:
    center2 = 10 ** 9
else:
    center2 = A[(N+2)//2]

ans1 = 0
for i in range(N):
    ans1 +=abs(A[i]-center1)
    
ans2 = 0
for j in range(N):
    ans2 += abs(A[j]-center2)
    
print (min(ans1, ans2))