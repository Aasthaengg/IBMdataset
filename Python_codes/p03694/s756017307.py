n = int(input())
a = [int(x) for x in input().split()]

A = list(set(a))
A.sort()

ans = 0
for i in range(1,len(A)):
    ans += A[i] - A[i-1]

print(ans)
