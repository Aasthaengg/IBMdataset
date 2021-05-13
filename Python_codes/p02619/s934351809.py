D=int(input())
c=list(map(int,input().split()))
s=[]
t=[]
last=[0]*26
v=0

for _ in range(D):
    ss=list(map(int,input().split()))
    s.append(ss)
for _ in range(D):
    tt=int(input())
    t.append(tt)

for d in range(D):
    last[t[d]-1]=d+1
    decrease=0
    for j in range(26):
        decrease+=c[j]*(d+1-last[j])
        
    v+=s[d][t[d]-1]-decrease
    print(v)