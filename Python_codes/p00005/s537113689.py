def gcd(a,b):
    while b != 0:
        a , b = b , a % b
    return a
def lcm(a,b):
    return int(abs(a*b) / gcd(a,b))

while True:
    try:
        a, b = [int(x) for x in input().split()]
    except:
        exit()
    print(gcd(a,b),lcm(a,b))