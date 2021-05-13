import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b=map(int, input().split())
    import fractions


    print(a*b//fractions.gcd(a,b))
resolve()