# -*- coding: utf-8 -*-

def main():

    N = int(input())
    H = list(map(int, input().split()))

    count = 0
    listA = []

    for i in range(N - 1):
        if H[i] >= H[i+1]:
            count += 1

        else:
            listA.append(count)
            count = 0

    listA.append(count)

    ans = max(listA)

    print(ans)


if __name__ == "__main__":
    main()