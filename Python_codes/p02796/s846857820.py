#!/usr/bin/env python3

def II(): return int(input())
def MII(): return map(int, input().split())
def LII(): return list(map(int, input().split()))

def main():
    N = II()

    xl = []
    for _ in range(N):
        X, L = MII()
        xl.append((X, L))
    
    xl = sorted(xl, key=lambda x: x[0])

    ans = 1
    r = xl[0][0] + xl[0][1]
    for x, l in xl[1:]:
        if r <= x - l:
            r = x + l
            ans += 1
        elif x + l <= r:
            r = x + l
       
    print(ans)


if __name__ == '__main__':
    main()
