n , m = map(int, input().split())
s = input()
t = input()

def gcd(num1,num2):
    r=1
    while r!=0:
        r=num1%num2
        num1=num2
        num2=r
    return num1

def lcm(num1,num2):
    return num1*num2//gcd(num1,num2)

g1 = lcm(n,m)
g2 = lcm(g1//n,g1//m)

for i in range(g1//g2):
    if s[g2*n*i//g1]!=t[g2*m*i//g1]:
        print('-1')
        exit()
print(g1)
