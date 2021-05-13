n = int(input())
s = input()
ans = 0
x = 0
for i in range(n):
    x += 1 if s[i] == "I" else -1
    ans = max(ans, x)
print(ans)