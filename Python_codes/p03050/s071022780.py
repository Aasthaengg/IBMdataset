import math


def main():
    n = int(input())
    a = []
    for i in range(1, (int)(math.sqrt(n)) + 1):
        if n % i == 0:
            if i != 1:
                a.append(i - 1)
            if n // i - 1 != 0:
                a.append((n // i) - 1)
    ans = 0
    for i in range(len(a)):
        if a[i] != 1 and (n // a[i] == n % a[i]):
            ans += a[i]
    print(ans)


main()
