
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    a, b = map(int, input().split())
    ans = a + b
    if ans >= 24:
        ans -= 24
    print(ans)


if __name__ == '__main__':
    main()