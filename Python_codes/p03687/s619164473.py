s = input()
L = []

ans = float('inf')
for l in s:
    cnl = 0
    anl = 0
    for s_ in s:
        if l == s_:
            anl = max(anl, cnl)
            cnl = 0
        else:
            cnl += 1
    anl = max(anl, cnl)
    ans = min(ans, anl)

print(ans)