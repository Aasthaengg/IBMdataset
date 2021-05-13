n=int(input())
r=0
b=0
for i in range(n):
 t=int(input())
 if i==0!=t or b+1<t:print(-1);exit()
 elif b>=t:r+=b
 b=t
print(r+b)