import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from collections import deque
def main():
    n, *a = map(int, read().split())
    a = deque(a)
    r = 1
    flag = False
    muki = 0
    n1 = a.popleft()
    while a:
        n2 = a.popleft()
        if flag:
            if n1 < n2 and muki:
                n1 = n2
            elif n1 > n2 and not muki:
                n1 = n2
            elif n1 == n2:
                pass
            else:
                r += 1
                flag = False
                n1 = n2
        else:
            if n1 < n2:
                flag = True
                muki = 1
                n1 = n2
            elif n1 > n2:
                flag = True
                muki = 0
                n1 = n2
    print(r)

if __name__ == '__main__':
    main()
