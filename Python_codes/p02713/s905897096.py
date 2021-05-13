import math


def main():
    K = int(input())
    s = 0
    for i in range(1, K+1):
        for j in range(1, K + 1):
            tmp = math.gcd(i, j)
            for k in range(1, K + 1):
                s += math.gcd(tmp, k)

    print(s)


if __name__=="__main__":
    main()
