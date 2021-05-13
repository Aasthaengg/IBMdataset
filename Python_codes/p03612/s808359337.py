import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    P = [0] + list(map(int, input().split()))
    same = deque()
    for i in range(1, N + 1):
        if i == P[i]: same.append(i)
    if not same:
        print(0)
        return

    ans = 0
    x = same.popleft()
    if not same:
        print(1)
        return
    while same:
        if same[0] - x == 1:
            same.popleft()
            ans += 1
            if same:
                x = same.popleft()
                if not same:
                    ans += 1
                    break
        else:
            ans += 1
            x = same.popleft()
            if not same:
                ans += 1
                break
    print(ans)


if __name__ == "__main__":
    main()
