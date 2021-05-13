n = int(input())
ans = float("inf")
for a in range(1, n):
    b = n-a
    ans = min(sum([int(i) for i in list(str(a)+str(b))]), ans)
print(ans)