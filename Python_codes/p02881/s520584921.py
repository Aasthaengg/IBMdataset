n=int(input())
ro=n**0.5
# print( ro )

maxi=1
for i in range(2, int(ro)+1):
    if n%i==0:
        maxi=i

print( maxi-1+n//maxi-1)
