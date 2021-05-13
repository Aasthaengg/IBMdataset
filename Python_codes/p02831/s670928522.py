# least common multiple
def lcms(*numbers):
    from math import gcd
    from functools import reduce
    def lcm_base(x, y):
        return (x * y) // gcd(x, y)
    return reduce(lcm_base, numbers)

def resolve():
    A, B = list(map(int, input().split()))
    print(lcms(A, B))



if '__main__' == __name__:
    resolve()