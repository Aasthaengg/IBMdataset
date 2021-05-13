s = input()
ans = 1000
for c in 'abcdefghijklmnopqrstuvwxyz':
    t = s
    if c not in t:
        continue
    tmp = 0
    while len(set(t)) > 1:
        res = ''
        for i in range(len(t)-1):
            if t[i] == c or t[i+1] == c:
                res += c
            else:
                res += '0'
        t = res
        tmp += 1
    ans = min(ans, tmp)

print(ans)