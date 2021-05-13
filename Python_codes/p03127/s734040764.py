import math

def main():
    _ = input()
    A = list(map(int, input().split()))
    ans = A[0]
    for a in A[1:]:
        ans = math.gcd(ans, a)
    print(ans)


if __name__ == '__main__':
    main()
