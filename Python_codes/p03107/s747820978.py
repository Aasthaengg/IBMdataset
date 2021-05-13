import sys
from collections import deque


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    S = list(map(int, list(input())))
    d_1 = deque(S[1:])
    d_2 = deque([S[0]])
    ans = 0
    for i in range(1, len(S)):
        if d_2:
            r = d_1.popleft()
            l = d_2.pop()
            if r != l:
                ans += 2
            else:
                d_2.append(l)
                d_2.append(r)
        else:
            d_2.append(d_1.popleft())
    print(ans)


if __name__ == '__main__':
    main()
