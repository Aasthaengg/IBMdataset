import sys
import bisect
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def main():

    n = int(input())
    s = list(input().strip())
    q = int(input())
    alpha = g = [[] for _ in range(26)]
    orda = ord('a')
    for i in range(n):
        alpha[ord(s[i])-orda].append(i)
    for i in range(q):
        a, b, c = map(str, input().split())
        if a == '1':
            b = int(b)-1
            if c != s[b]:
                alpha[ord(s[b])-orda].remove(b)
                s[b] = c
                bisect.insort(alpha[ord(c)-orda], b)
        else:
            ans = 0
            for i in range(26):
                if len(alpha[i]) > 0:
                    it = bisect.bisect_left(alpha[i], int(b)-1)
                    if it < len(alpha[i]) and alpha[i][it] < int(c):
                        ans += 1
            print(ans)


main()
