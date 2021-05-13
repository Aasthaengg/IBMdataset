#!/usr/bin/env python3

def solve(a,b,k):
    l = []
    for i in range(min(a,b)):
        if a % (i+1) == 0 and b % (i+1) == 0:
            l.append(i+1)
    return(l[-k])

def main():
    A,B,K =map(int,input().split())
    print(solve(A,B,K))


if __name__ == '__main__':
    main()