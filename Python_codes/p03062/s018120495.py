N = int(input())
A = list(map(int,input().split()))

minuscount = 0
for i in range(0,N,1):
    if A[i] < 0:
        minuscount +=1
    if A[i]==0:
        minuscount = 0
        break

ans = 0
for i in range(0,N,1):
    ans += abs(A[i])

minabs = 10**10
if minuscount % 2 !=0:
    for i in range(0,N,1):
        minabs = min(minabs,abs(A[i]))
    ans -= 2*minabs

print(ans)