N,M=map(int,input().split())
k=[list(map(int,input().split())) for _ in range(M)] 
*p,=map(int,input().split())
t=0
a=0
for i in range(2 ** N):
 t=sum(1 for j in range(M) if sum(1 for h in k[j][1:] if i>>(h-1)&1)%2==p[j])
 if t==M:a+=1
print(a)