import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=input()
    a='Sunny'
    b='Cloudy'
    c='Rainy'
    if s==a:
        print(b)
    elif s==b:
        print(c)
    else:
        print(a)
resolve()