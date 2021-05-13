readline = open(0).readline
ans = []
while 1:
    m, f, r = map(int, readline().split())
    if m == f == r == -1:
        break
    v = m+f
    if m == -1 or f == -1 or v < 30:
        ans.append("F\n")
    elif v >= 80:
        ans.append("A\n")
    elif v >= 65:
        ans.append("B\n")
    elif v >= 50 or (v >= 30 and r >= 50):
        ans.append("C\n")
    else:
        ans.append("D\n")
open(1, 'w').writelines(ans)
