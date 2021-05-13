
h,w = map(int, input().split())
n = int(input())
a = [int(i) for i in input().split()]
con = 1
d = []

for i in a:
    for j in range(i):
        d.append(con)
    con += 1

whi = 0
for i in range(h):
    if whi == 0:
        a = d[i*w:w+w*i]
        L=[str(j) for j in a]
        L=' '.join(L)
        print(L)
        whi = 1
    else:
        a = d[i*w:w+w*i]
        a.reverse()
        L=[str(j) for j in a]
        L=' '.join(L)
        print(L)
        whi = 0