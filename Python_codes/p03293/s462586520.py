import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def main():
    S = deque(input())
    T = deque(input())
    same = False
    for _ in range(len(S)):
        if S == T:
            same = True
            break
        c = S.popleft()
        S.append(c)
    if same: print("Yes")
    else: print("No")


if __name__ == "__main__":
    main()
