n,m=map(int,input().split())
s=input() ;a=len(s)
t=input() ;b=len(t)
def gcd(a,b):
    if b==0: return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return a*b//gcd(a,b)
L=lcm(len(s),len(t))

d={}
now=0
for i in range(0,L,L//a):
    d[i]=s[now]
    now+=1
now=0
for j in range(0,L,L//b):
    if d.get(j, t[now])!=t[now]:
        print(-1);exit()
    now+=1
print(L)