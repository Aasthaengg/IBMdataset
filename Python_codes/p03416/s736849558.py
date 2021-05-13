#!/usr/bin/env python3

def judge(k):
    n = str(k)
    return n[0] == n[4] and n[1] == n[3]

def solve(a,b):
    c = 0
    for i in range(a,b+1):
        if judge(i):
            c += 1
    return c 

def main():
    A,B = map(int,input().split())
    print(solve(A,B))

if __name__ == '__main__':
    main()