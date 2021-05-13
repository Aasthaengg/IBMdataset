import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    S = input()
    K = int(input())
    ans = ''
    for s in S:
        if s=='a':
            ans += s
        else:
            if 123 - ord(s) <= K:
                ans += 'a'
                K -= 123 - ord(s)
            else:
                ans += s
    if K > 0:
        ans = ans[:-1] + (chr(ord(ans[-1]) + K%26))
    print(ans)


if __name__ == '__main__':
    main()
