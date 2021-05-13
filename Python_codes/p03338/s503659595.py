import collections

n = int(input())
s = input()

# c = collections.Counter(s)
# print(c)

ans = 0
for i in range(1, n):
    a = s[:i]
    b = s[i:]
    ca = list(collections.Counter(a).keys())
    cb = list(collections.Counter(b).keys())
    c = 0
    for cai in ca:
        if cai in cb:
            c += 1
    if ans < c:
        ans = c

print(ans)
