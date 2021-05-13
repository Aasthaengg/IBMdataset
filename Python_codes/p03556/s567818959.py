N = int(input())
ans = 1
while ans * ans <= N:
    ans += 1
ans -= 1
print(ans * ans)
