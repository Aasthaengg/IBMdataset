from itertools import accumulate

N = int(input())
A = [int(i) for i in input().split()]

B = list(accumulate(A))
p = B[-1]
ans = 10**12
for i in range(N-1):
    ans = min(ans,abs(p-2*B[i]))

print(ans)
