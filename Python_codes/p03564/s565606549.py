a = int(input())
b = int(input())
ans = 1
for _ in range(a):
    if ans < b:
        ans *= 2
    else:
        ans += b
print(ans)