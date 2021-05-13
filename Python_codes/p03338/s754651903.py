n = int(input())
s = input()

ans = 0
for div in range(n):
    left = set(s[:div])
    right = set(s[div:])
    tmp = 0
    for i in left:
        if i in right:
           tmp += 1
    ans = max(ans, tmp)
print(ans)
