n = int(input())
s = [input() for _ in range(n)]
ss = sorted(s)
t = ss
x = 0
maxx = 0
for i in range(n-1):
    if ss[i] == ss[i+1]:
        x += 1
        if x == maxx:
            maxx = x
            t.append(ss[i])
        elif x > maxx:
            maxx = x
            t = [ss[i]]
    else:
        x = 0
for j in t:
    print(j)