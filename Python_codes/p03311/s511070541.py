N = int(input())
A = [int(i) for i in input().split()]
for i in range(N):
    A[i] = A[i] - (i+1)
A.sort()
b = A[N//2]
ans = 0
for a in A:
    ans += abs(a - b)
print(ans)
