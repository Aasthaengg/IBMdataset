blue={}
red={}
n=int(input())
for i in range(n):
    s=input()
    blue[s]=blue.get(s,0)+1
m=int(input())
for i in range(m):
    t=input()
    red[t]=red.get(t,0)+1

mx=0
for k,v in blue.items():
    mx=max(mx,blue[k]-red.get(k,0))
print(mx)
