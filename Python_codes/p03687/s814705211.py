s = input()
l = len(s)

c = set([])
for x in s:
    c.add(x)

def solve(arg):
    res = 0
    id = -1
    for i in range(l):
        if s[i] == arg:
            if res < i - id - 1:
                res = i - id - 1
            id = i
    if l - id - 1 > res:
        res = l - id - 1
    return res

ans = 1001001
for x in c:
    tmp = solve(x)
    if tmp < ans:
        ans = tmp

print(ans)
