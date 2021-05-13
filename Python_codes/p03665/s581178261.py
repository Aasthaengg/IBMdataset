N, P = map(int, input().split())
A = list(map(int, input().split()))
even = 0
odd = 0
for i in range(N):
    if A[i]%2==0:
        even += 1
    else:
        odd += 1
if odd>=1:
    ans = pow(2,even+odd-1)
elif P==0:
    ans = pow(2,even)
else:
    ans = 0
print(ans)