p=input()
q=input()
q=2*q
s=len(p)
u=0
l=len(q)
for i in range(l):
    if p==q[i:s+i]:
        print("Yes")
        u=1
        break
if u==0:
    print("No")