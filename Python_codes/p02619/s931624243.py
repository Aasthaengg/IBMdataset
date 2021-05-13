D=int(input())
*c,=map(int,input().split())
s=[]
for i in range(D):
    *x,=map(int,input().split())
    s.append(x)
T=[]
for i in range(D):
    T.append(int(input()))

last=[-1]*26
v=0
for d in range(D):
    v+=s[d][T[d]-1]
    last[T[d]-1]=d
    for i in range(26):
        v-=c[i]*(d-last[i])
    print(v)