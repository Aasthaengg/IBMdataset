n = int(input())
A = list(map(int, input().split()))

ans = 10**11
sum_A = sum(A)
l = 0

for a in A:
    l += a
    if abs(l - (sum_A - l)) < ans:
        ans = abs(l - (sum_A - l))

print(ans)
