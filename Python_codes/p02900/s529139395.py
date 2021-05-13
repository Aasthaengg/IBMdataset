from fractions import gcd

a,b=map(int,input().split())

gcd=gcd(a,b)
ab_gcd=gcd

f=[]
for i in range(2,int(ab_gcd**0.5)+1):
    while gcd%i==0:
        gcd=gcd//i
        f.append(i)
if gcd!=1:
    f.append(gcd)

print(len(set(f))+1)
