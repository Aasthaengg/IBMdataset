a = list(input())
l = len(a)
alphcnt = [0] * 26
for i in a:
    alphcnt[ord(i) - 97] += 1
ans = (l * (l + 1)) // 2 + 1
for i in alphcnt:
    ans -= (i * (i + 1)) // 2
print(ans)