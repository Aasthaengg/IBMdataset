n = int(input())
ans = 1
for i in range(100000):
    if i * i <= n:
        ans = i * i
    else: break
print(ans)