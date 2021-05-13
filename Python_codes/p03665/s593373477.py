import math
def main():
    N, P = map(int, input().split())
    A = [int(a) for a in input().split()]
    modA = list()

    for a in A:
        modA.append(a % 2)

    zero = modA.count(0)
    one = modA.count(1)

    ans = tmp = 0
    f = math.factorial
    if P == 0:
        for i in range(0, one + 1, 2):
            tmp += f(one) // (f(i) * f(one - i))
    else:
        for i in range(1, one + 1, 2):
            tmp += f(one) // (f(i) * f(one - i))

    if zero > 0:
        ans = tmp * 2 ** zero
    else:
        ans = tmp

    print(ans)

if __name__ == "__main__":
    main()