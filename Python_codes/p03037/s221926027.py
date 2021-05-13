#n=int(input())
#s,t=input().split()
n,m = map(int, input().split())
#l=list(map(int, input().split()))
l=[0]*100005
r=[1000005]*100005
z=1000010
for i in range(m):
   l[i],r[i]=map(int,input().split()) 
mi=max(l)
ma=min(r)



if mi>ma:
    print(0)
else:
    print(ma-mi+1)