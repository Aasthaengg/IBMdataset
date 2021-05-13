n = int(input())

M = pow(10, 9) + 7
import sys

dc = {}
al = [0]

rr = [1]


def search(ss, start, end):
    z = al[(start + end)//2]
    nz = al[(start + end)//2+1]
    if z <= ss and ss < nz:
        return (start+end)//2
    elif ss < z:
        return search(ss, start, (start+end)//2)
    else:
        return search(ss, (start+end)//2+1, end)

c = 0
cn = 0
for line in sys.stdin:
    a = int(line)
    if a in dc:
        ss = dc[a]
        if ss != c-1:
            if ss >= al[cn]:
                rr.append((rr[cn]*2)%M)
            else:
                i = search(ss, 0, cn)
                rr.append((rr[cn] + rr[i])%M)
            al.append(c)
            cn += 1
    dc[a] = c
    c += 1
print(rr[cn]%M)
