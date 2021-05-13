l, r, D = input().split()
L=int(l)
R=int(r)
d=int(D)
s=0
for i in range(L,R+1):
    if i%d==0:
        s=s+1
print(s)        