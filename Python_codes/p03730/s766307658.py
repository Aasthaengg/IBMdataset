from fractions import gcd
def check():
    A, B, C = map(int, input().split())
    if C%gcd(A,B)==0:
        return 'YES'
    return 'NO'
print(check())