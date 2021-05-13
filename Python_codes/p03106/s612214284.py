def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))
  

def gcd(a, b):
    """最大公約数"""
    if b == 0: return a
    return gcd(b, a % b)


def main():
    a, b, k = Input()
    k -= 1
    data = sorted((i for i in range(1, gcd(a, b)+1)
                   if a % i == 0 and b % i == 0), reverse=True)

    print(data[k])

main()