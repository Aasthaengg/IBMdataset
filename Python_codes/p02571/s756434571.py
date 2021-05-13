s = str(input())
t = str(input())
a = []
for i in list(s):
    a.append(i)
b = []
for j in list(t):
    b.append(j)
c = len(a)
d = len(b)
w = 1000
for k in range(c-d+1):
    e = a[k:k+d]
    f = 0
    for l in range(d):
        if e[l] != b[l]:
            f= f+1
    if w > f:
         w= f
print(w)