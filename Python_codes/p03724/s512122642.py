import sys
def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())

from collections import deque
def main():
    n, m = mi()
    cc = [0]*n
    for _ in range(m):
        a, b = mi()
        a -= 1
        b -= 1 
        cc[a] += 1
        cc[b] += 1
    for x in cc:
        if x%2 == 1:
            print('NO')
            return
    print('YES')



if __name__ == '__main__':
    main()