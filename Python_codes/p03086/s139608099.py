#!/usr/bin/env python3

def II(): return int(input())
def MII(): return map(int, input().split())
def LII(): return list(map(int, input().split()))

def main():
    S = input()
    S += "$"

    ans = 0 
    cnt = 0
    for s in S: 
        if s in ('A', 'T', 'C', 'G'):
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0

    print(ans)

if __name__ == '__main__':
    main()
