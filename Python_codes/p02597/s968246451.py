from sys import stdin

input = stdin.readline
import math

def solve():
    n = int(input())
    a = list(input().strip())
    left = 0
    rpos = [i for i in range(n) if a[i] == 'R']
    if not rpos:
        print(0)
        return
    right = len(rpos) - 1
    cnt = 0
    while right >= 0 and left < rpos[right]:
        if a[left] == 'W':
            cnt += 1
            right -= 1
        left += 1
    print(cnt)

if __name__ == '__main__':
    solve()
