def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return (a*b)//gcd(a,b)
n=int(input())
t=[]
for i in range(n):
    tmp=int(input())
    if tmp in t:
        continue
    t.append(tmp)

ans=1
for i in t:
    ans=lcm(ans,i)
print(ans)