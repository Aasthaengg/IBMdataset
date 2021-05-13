L = str(input())
ans = 0
for i in range(4):
    if L[i] == '+':
        ans += 1
    else:
        ans -= 1

print(ans)
