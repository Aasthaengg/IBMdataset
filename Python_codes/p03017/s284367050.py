n,a,b,c,d=map(int,input().split())
a-=1
b-=1
c-=1
d-=1
s=input()
bl_bl=[]
jump=[]
ans=1

for i in range(1,n-1):
    if s[i-1:i+1]=="##":
        if a<i<c or b<i<d:
            ans=2
            break
    if s[i-1:i+2]=="...":
        jump.append(i)

if ans!=2:
    if c<d:
        ans=0
    else:
        for i in jump:
            if b<=i<=d:
                ans=0
                break

print("Yes" if ans==0 else "No") 