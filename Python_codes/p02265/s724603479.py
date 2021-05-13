import sys
import array
from collections import deque


def main():
    n = int(input())
    #l = array.array('L')
    l = deque()
    for _ in range(n):
        c = sys.stdin.readline().split()
        if c[0] == "insert":
            l.appendleft(int(c[1]))
        elif c[0] == "delete":
            if int(c[1]) in l:
                l.remove(int(c[1]))
        elif c[0] == "deleteFirst":
            l.popleft()
        elif c[0] == "deleteLast":
            l.pop()
    print(*l)


if __name__ == "__main__":
    main()
