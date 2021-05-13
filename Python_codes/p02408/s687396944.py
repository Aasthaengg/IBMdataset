marks='SHCD'
n=input()
card=[raw_input().split() for _ in range(n)]
m={}
for mk,rk in card:
    m.setdefault(mk,[0]*14)
    m[mk][int(rk)]=1
for i in range(len(m)):
    k=marks[i]
    v=m[k]
    for j in range(1,14):
        if not v[j]: print k,j