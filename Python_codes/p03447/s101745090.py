#!/usr/bin/env python3

def main():
    #N = map(int, open(0).read().split())
    x = int(input())
    a = int(input())
    b = int(input())

    ans = (x-a)%b
    print(ans)



main()
