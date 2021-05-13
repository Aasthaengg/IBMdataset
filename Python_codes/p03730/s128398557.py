a,b,c=map(int,input().split())
#GCD of a,b
gcd=1
for i in range(2,100):
    if a%i==0 and b%i==0:
        gcd=max(gcd,i)
#print(gcd)
if c%gcd==0:
    print("YES")
else:
    print("NO")
