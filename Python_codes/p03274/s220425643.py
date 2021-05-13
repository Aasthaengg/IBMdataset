import sys
def input(): return sys.stdin.readline().rstrip()

def solve(l, r):
    lv = abs(l)
    rv = abs(r)
    if (l < 0) ^ (r < 0):
        return lv + rv + min(lv, rv)
    else:
        return max(lv, rv)

def main():
    N, K = map(int, input().split())
    x = tuple(map(int, input().split()))

    ans = 10 ** 9
    for i in range(N - K + 1):
        tmp_ans = solve(x[i], x[i + K - 1])
        if tmp_ans < ans:
            ans = tmp_ans

    print(ans)

if __name__ == '__main__':
    main()
