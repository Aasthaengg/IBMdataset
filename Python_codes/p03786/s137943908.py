from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
A.sort()
accumA = [*accumulate(A)]
check = [0] * (N-1)
for i in range(N-1):
    if A[i+1] <= 2*accumA[i]:
        check[i] = 1
ans = 1
j = N-2
while check[j]:
    ans += 1
    j -= 1
    if j == -1:
        break
print(ans)