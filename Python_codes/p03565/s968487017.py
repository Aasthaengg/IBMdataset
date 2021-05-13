s = input()
t = input()

ans = 'UNRESTORABLE'
def test(i):
    for ns, nt in zip(s[i:i+len(t)], t):
        if ns == '?':
            continue
        if ns != nt:
            return False
    return True

for i in range(len(s) - len(t) + 1):
    if test(i):
        re_s = s.replace('?', 'a')
        ans = re_s[:i] + t + re_s[i+len(t):]

print(ans)
