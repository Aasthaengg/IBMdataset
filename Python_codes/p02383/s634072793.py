ns=list(map(int,input().split()))
rs=input()

def rot(d, r):
    if r == 'N':
        return [d[1], d[5], d[2], d[3], d[0], d[4]]
    if r == 'E':
        return [d[3], d[1], d[0], d[5], d[4], d[2]]
    if r == 'W':
        return [d[2], d[1], d[5], d[0], d[4], d[3]]
    if r == 'S':
        return [d[4], d[0], d[2], d[3], d[5], d[1]]
    return d

for r in rs:
    ns = rot(ns, r)

print(ns[0])