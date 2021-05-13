import sys

def input():
    return sys.stdin.readline().strip()

def main():

    Q = int(input())
    ma = 10 ** 5 + 1
    dp = [0] * ma
    dp[2] = 1

    for i in range(3,ma,2):
        if dp[i] == 0:
            dp[i] = 1
            if dp[(i + 1) // 2] == 1 or dp[(i + 1) // 2] == 2:
                dp[i] = 2
            for j in range(i * 2,ma,i):
                dp[j] = 3

    ruiseki = [0] * ma

    for i in range(1,ma):
        if dp[i] == 2:
            ruiseki[i] = ruiseki[i-1] + 1
        else:
            ruiseki[i] = ruiseki[i-1]

    for _ in range(Q):
        l,r = map(int,input().split())
        print(ruiseki[r] - ruiseki[l-1])

if __name__ == "__main__":
    main()