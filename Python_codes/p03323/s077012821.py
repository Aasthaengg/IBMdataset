#!/usr/bin/env python3

def main():
    a, b = map(int,input().split())
    space = 16 - (a + b)
    gap = abs(a-b)
    if gap <= -(-space // 2):
        print("Yay!")
    else:
        print(":(")

main()