s = input()
t = input()
ls = len(s)
lt = len(t)
r = lt
for i in range(ls - lt + 1):
    tmp = 0
    for j in range(lt):
        if s[i + j] != t[j]: tmp += 1
    r = min(r, tmp)
print(r)
