#!/usr/bin/env python3

def solve(h,w,s):
    for i in range(1,h):
        for j in range(1,w):
            if s[i][j] == "#" and \
               s[i+1][j] != "#" and \
               s[i-1][j] != "#" and \
               s[i][j+1] != "#" and \
               s[i][j-1] != "#":
                return "No"
    return "Yes"



def main():
    H,W = map(int,input().split())
    s = ['.'*55]*55
    for i in range(H):
        s[i] = input() + '.'*(55-W)
    print(solve(H,W,s))
    return

if __name__ == '__main__':
    main()
