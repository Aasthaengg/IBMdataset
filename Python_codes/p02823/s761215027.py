#!/usr/bin/env python3

def f(n,a,b):
    if (a + b) % 2:
        return min(a-1,n-b) + 1 + (b-a-1)//2
    else:
        d = b-a
        return d//2

def main():
    N,A,B = map(int,input().split())
    print(f(N,A,B))

if __name__ == '__main__':
    main()