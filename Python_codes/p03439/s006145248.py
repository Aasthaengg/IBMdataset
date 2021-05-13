import sys
n = int(input())
print(0)#, flush=True)
s = input()
if s == "Vacant":
    sys.exit()
l = 0
r = n
ls = s
rs = s

def nibun(l, r, m, ls, rs, s):
    if ((m-l) % 2 == 0 and ls == s) or\
        ((m-l) % 2 == 1 and ls != s):
        return 1
    else:
        return 0

for ii in range(21):
    m = (l+r)//2
    print(m)#, flush=True)
    s = input()
    if s == "Vacant":
        break
    if nibun(l, r, m, ls, rs, s) == 0:
        r = m
        rs = s
    else:
        l = m
        ls = s