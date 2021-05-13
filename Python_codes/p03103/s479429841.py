f=lambda:map(int,input().split());n,m=f();c=0
for a,b in sorted(list(f())for _ in range(n)):t=min(b,m);c+=a*t;m-=t
print(c)