s = list(input())

ans = 0
x = len(s) - 1
for i in range(len(s) - 1, -1, -1):
    if s[i] == "B":
        ans += x - i
        x -= 1

print(ans)