N = int(input())
A = list(map(int, input().split()))

A.sort()

ans = 0
total = A[0]
for i in range(N-1):
    if total*2 >= A[i+1]:
        ans += 1
    else:
        ans = 0
    total += A[i+1]

print(ans+1)
