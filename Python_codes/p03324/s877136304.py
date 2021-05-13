d,n=input().split()
if n=="100":
    n="101"
d=int(d)
for i in range(d):
    n+="00"
print(n)