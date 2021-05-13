import sys
input = sys.stdin.readline
from collections import deque
def main():
    A = deque(list(input().rstrip()))
    B = deque(list(input().rstrip()))
    C = deque(list(input().rstrip()))
    A.append('e')
    B.append('e')
    C.append('e')
    tmp = A.popleft()
    last = ''
    while True:
        if tmp == 'e':
            print(last.upper())
            return
        if tmp == 'a':
            last = tmp
            tmp = A.popleft()
        if tmp == 'b':
            last = tmp
            tmp = B.popleft()
        if tmp == 'c':
            last = tmp
            tmp = C.popleft()

if __name__ == '__main__':
    main()