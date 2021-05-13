
def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
def lcm(a,b): 
    return (a*b) / gcd(a,b) 

a,b = input().split()
a = int(a)
b = int(b)
print(int(lcm(a,b)))