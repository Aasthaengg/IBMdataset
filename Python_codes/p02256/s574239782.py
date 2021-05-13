"""
最大公約数を求める
"""
def gcd(a, b):
    while (a != 0 and b != 0):
        if (a >= b):
            a = a % b
        else:
            b = b % a
    return a+b

if __name__ == '__main__':
    x, y = map(int, input().split())
    print(gcd(x,y))

