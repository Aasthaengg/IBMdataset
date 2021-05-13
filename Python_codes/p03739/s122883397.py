# vim: fileencoding=utf-8


def main():
    n = int(input())
    a = list(map(int, input().split()))

    evenAns, oddAns = 0, 0
    evenTotal, oddTotal = 0, 0

    # 奇数を負に
    for i in range(n):
        oddTotal += a[i]
        if i % 2 == 0:
            if oddTotal <= 0:
                oddAns += abs(oddTotal) + 1
                oddTotal += abs(oddTotal) + 1
        else:
            if oddTotal >= 0:
                oddAns += abs(oddTotal + 1)
                oddTotal -= abs(oddTotal) + 1

    # 偶数を負に
    for i in range(n):
        evenTotal += a[i]
        if i % 2 == 1:
            if evenTotal <= 0:
                evenAns += abs(evenTotal) + 1
                evenTotal += abs(evenTotal) + 1
        else:
            if evenTotal >= 0:
                evenAns += abs(evenTotal) + 1
                evenTotal -= abs(evenTotal) + 1
    print(min(evenAns, oddAns))


if __name__ == "__main__":
    main()
