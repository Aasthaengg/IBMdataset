import fractions
def lcm(x,y):
    return (x*y)//fractions.gcd(x,y)
n=int(input())
t=[0]*n
num=1
for i in range(n):
    t[i]=int(input())
    num=lcm(num,t[i])
print(num)
