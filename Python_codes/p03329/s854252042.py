#!/usr/bin/env python3
def main():
    N = int(input())
    
    can_six = []
    can_nine = []
    limit = 100
    for i in range(1, limit):
        six = 6 ** i
        if six <= N:
            can_six.append(six)
        nine = 9 ** i
        if nine <= N:
            can_nine.append(nine)
        if six > N and nine > N:
            break
    can = sorted([1] + can_six + can_nine)

    INF = 10 ** 9
    dp = [INF] * (N + 1)
    dp[0] = 0
    for n in range(N + 1):
        for draw in can:
            if n - draw < 0:
                break
            dp[n] = min(dp[n], dp[n - draw] + 1)
    print(dp[-1])


if __name__ == '__main__':
    main()
