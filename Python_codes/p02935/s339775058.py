N = int(input())
*A, = map(int, input().split())
A.sort()
ans = (A[0]+A[1])/2
for a in A[2:]:
    ans = (ans+a)/2
print(ans)
