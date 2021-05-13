from sys import stdin

input = stdin.readline
import math

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    cur = 0
    for i in a:
        cur = math.gcd(i, cur)
    if cur > 1:
        print('not coprime')
        return
    m = max(a)
    prime = [True] * (m+1)
    c = {}
    for i in a:
        c[i] = c.get(i,0) + 1
    for i in range(2,m+1):
        if prime[i]:
            cnt = 0
            for j in range(i,m+1,i):
                prime[j] = False
                cnt += c.get(j,0)
                if cnt > 1:
                    print('setwise coprime')
                    return
    print('pairwise coprime')
if __name__ == '__main__':
    solve()
