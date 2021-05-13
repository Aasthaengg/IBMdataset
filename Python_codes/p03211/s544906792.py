s = input()
l = len(s)
ans = 999
for i in range(l - 2):
    a = int(s[i:i + 3])
    b = abs(753 - a)
    if b < ans:
        ans = b
print(ans)
