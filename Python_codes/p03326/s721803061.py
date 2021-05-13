import sys

sys.setrecursionlimit(50000)

n, m = (int(i) for i in input().strip().split(" "))
xs = []
ys = []
zs = []
for i in range(n):
    a, b, c = (int(i) for i in input().strip().split(" "))
    xs.append(a)
    ys.append(b)
    zs.append(c)

k=0

ar=[]
for i in range(n):
    ar.append(xs[i]+ys[i]+zs[i])
ar.sort(reverse=True)
t=sum(ar[:m])
if t>k:
    k=t

ar=[]
for i in range(n):
    ar.append(xs[i]+ys[i]-zs[i])
ar.sort(reverse=True)
t=sum(ar[:m])
if t>k:
    k=t

ar=[]
for i in range(n):
    ar.append(xs[i]-ys[i]+zs[i])
ar.sort(reverse=True)
t=sum(ar[:m])
if t>k:
    k=t

ar=[]
for i in range(n):
    ar.append(-1*xs[i]+ys[i]+zs[i])
ar.sort(reverse=True)
t=sum(ar[:m])
if t>k:
    k=t

ar=[]
for i in range(n):
    ar.append(xs[i]-ys[i]-zs[i])
ar.sort(reverse=True)
t=sum(ar[:m])
if t>k:
    k=t

ar=[]
for i in range(n):
    ar.append(-xs[i]+ys[i]-zs[i])
ar.sort(reverse=True)
t=sum(ar[:m])
if t>k:
    k=t

ar=[]
for i in range(n):
    ar.append(-xs[i]-ys[i]+zs[i])
ar.sort(reverse=True)
t=sum(ar[:m])
if t>k:
    k=t

ar=[]
for i in range(n):
    ar.append(-xs[i]-ys[i]-zs[i])
ar.sort(reverse=True)
t=sum(ar[:m])
if t>k:
    k=t
print(k)

