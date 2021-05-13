a = input()
b = input()
ans = 0
for i in range (0,3):
    if a[i] == b[i]:
        ans = ans + 1
print(ans)