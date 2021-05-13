d=int(input())
s=int(d**0.5)
if s*s!=d:
    s+=1
t=s*s-d
for i in range(int(t**0.5)+3,0,-1):
    if t%i==0:
        print(s,i,t//i,s,0,0)
        break