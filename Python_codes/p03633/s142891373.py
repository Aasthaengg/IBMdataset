def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

n=int(input())
a=[]
temp=int(input())
a.append(temp)
g=temp

for _ in range(n-1): #O(nlogt)
    temp=int(input())
    a.append(temp)
    gc=gcd(max(g,temp),min(g,temp))
    g=g*(temp//gc)

print(g)