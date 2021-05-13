n = int(input())
A = sorted(map(int, input().split()))
diff = float("inf")
ans = 0
for a in A[:-1]:
    d = abs(a - A[-1] / 2)
    if d < diff:
        ans = a
        diff = d
print(A[-1], ans)
