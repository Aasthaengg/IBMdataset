s = input()[::-1]
n = len(s)
tmp = 0
ans = 0
for i in range(n):
    if s[i] == 'S':
        tmp += 1
    else:
        tmp -= 1
    ans = max(ans, tmp)

print(ans * 2)