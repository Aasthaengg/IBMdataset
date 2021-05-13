import sys
input = sys.stdin.readline


# 約数を列挙 (ex. 6 => [1,2,3,6])
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors


def main():
    N = int(input())
    D = make_divisors(N)
    D.remove(1)
    ans = 0
    for a in D:
        q, r = divmod(N, a-1)
        if q == r:
            ans += a-1
    print(ans)


if __name__ == '__main__':
    main()
