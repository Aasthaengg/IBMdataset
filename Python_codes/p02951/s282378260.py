A, B, C = list(map(int, input().split()))

a = A - B
ans = 0
if a >= C:
    ans = 0
else:
    ans = C - a
print(ans)