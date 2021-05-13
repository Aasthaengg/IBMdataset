import sys
input = sys.stdin.readline

def main():
    N = int(input())
    s = [input().strip() for i in range(2)]

    MOD = 1000000007
    if N == 1:
        print(3)
        return
    ans = 0
    pre = -1
    i = 0
    while i < N-1:
        if s[0][i] == s[0][i+1]:# type 0
            if ans == 0:
                ans = 6
            else:
                if pre == 0:
                    ans *= 3
                    ans %= MOD
                else:
                    ans *= 2
                    ans %= MOD
            i += 2
            pre = 0
        else:# type 1
            if ans == 0:
                ans = 3
            else:
                if pre == 0:
                    pass
                else:
                    ans *= 2
                    ans %= MOD
            i += 1
            pre = 1
    if i == N-1:
        if pre == 1:
            ans *= 2
            ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()