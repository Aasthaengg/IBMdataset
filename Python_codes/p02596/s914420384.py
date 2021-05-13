from sys import stdin

input = stdin.readline
import math

def solve():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        return
    cnt = 1
    cur = 7
    while True:
        r = cur % k
        if r == 0:
            print(cnt)
            break
        cur = r * 10 + 7
        cnt += 1

if __name__ == '__main__':
    solve()
