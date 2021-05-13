# -*- coding: utf-8 -*-

def main():

    N, X = map(int, input().split())
    m = []
    for i in range(N):
        m.append(int(input()))

    sumM = 0
    ans = 0

    flag = False

    for i in m:
        sumM += i
        ans += 1

    remain = X - sumM

    minM = min(m)

    remainNum = remain // minM

    ans += remainNum

    print(ans)


if __name__ == "__main__":
    main()