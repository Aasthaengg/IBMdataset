import fractions
n,m=map(int,input().split())
s=list(str(input()))
t=list(str(input()))

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

l=lcm(n, m)
index=fractions.gcd(n,m)
#print(indexn,indexm)
for i in range(index):
    #print(i)
    if s[n//index*i]!=t[m//index*i]:
        print(-1)
        break
else:
    print(l)