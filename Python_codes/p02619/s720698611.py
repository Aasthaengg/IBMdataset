s=list()
t=list()
v=list()
last=[0]*26
D=int(input())
c=list(map(int,input().split()))
for i in range(D):
    s.append(list(map(int,input().split())))
for i in range(D):
    t.append(int(input()))
legacy=0
for i in range(D):
    minus=0
    v.append(legacy)
    v[i]+=s[i][t[i]-1]
    last[t[i]-1]=i+1
    for j in range(26):
        minus+=c[j]*(i+1-last[j])
    v[i]-=minus
    legacy=v[i]
for i in range(D):
    print(v[i])