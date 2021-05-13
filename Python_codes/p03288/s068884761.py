#!/usr/bin/env python3
def solve(R: int):
    ans = ["ABC", "ARC", "AGC"]
    if R < 1200:
        print(ans[0])
    elif 1200 <= R < 2800:
        print(ans[1])
    else:
        print(ans[2])

def main():
    R = int(input())
    solve(R)

if __name__ == '__main__':
    main()
