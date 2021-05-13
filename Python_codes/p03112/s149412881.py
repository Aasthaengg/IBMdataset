from bisect import bisect_left
from sys import stdin
input = stdin.buffer.readline

def main():
    a, b, q = map(int, input().split())
    s = [int(input()) for _ in range(a)]
    t = [int(input()) for _ in range(b)]
    x = [int(input()) for _ in range(q)]

    ans = [0] * q
    for i in range(q):
        start = x[i]
        si = bisect_left(s, start, hi=a-1)
        ti = bisect_left(t, start, hi=b-1)

        sl = (s[si-1], s[si])
        tl = (t[ti-1], t[ti])

        distance = 100000000000
        for j in sl:
            for k in tl:
                if abs(start - j) + abs(j - k) < distance:
                    distance = abs(start - j) + abs(j - k)
                if abs(start - k) + abs(k - j) < distance:
                    distance = abs(start - k) + abs(k - j)

        ans[i] = distance

    for i in ans:
        print(i)

main()