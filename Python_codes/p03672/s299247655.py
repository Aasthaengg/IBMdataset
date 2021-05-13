s = input()

ans = 0
n = len(s) // 2

for i in range(n-1):
    if s[0 : i] == s[i+1 : i+1 + i]:
        ans = i + 1

print(ans * 2)
