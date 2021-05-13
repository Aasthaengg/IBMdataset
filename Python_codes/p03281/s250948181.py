import sys
input = sys.stdin.readline


def divisors(num):
    array = []
    limit = int(num ** 0.5) + 1
    for i in range(1, limit):
        if num % i == 0:
            div1 = i
            div2 = num//i
            array.append(div1)
            if div1 != div2:
                array.append(div2)
    array.sort()
    return array


def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1, 2):
        count = len(divisors(i))
        if count == 8:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
