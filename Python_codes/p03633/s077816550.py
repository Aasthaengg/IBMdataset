def gcd(a,b):
    if a < b:
        a,b = b,a
    if b != 0:
        return gcd(b,a%b)
    return a

def solve(n,ts):
    a = ts[0]
    for i in range(n):
        b = ts[i]
        c = gcd(a,b)
        a = a*b//c
    return a

if __name__ == '__main__':
    n = int(input())
    ts = [int(input()) for i in range(n)]
    print(solve(n,ts))