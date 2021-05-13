#coding:UTF-8

def gcd(x,y):
    r = x % y

    if r==0: return y
    else: return gcd(y,r)

def lcm(x,y):
    return x * y / gcd(x,y)

while True:
    try:
        n = map(int, raw_input().split())

        print "%d %d"%(gcd(n[0],n[1]),lcm(n[0],n[1]))

    except Exception:
        break;