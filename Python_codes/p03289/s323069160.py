#!/usr/bin/env python3

def solve(s):
    return s[0] == "A" and s.count("C",2,-1) == 1 and s[1:].replace("C", "").islower()


def main():
    S = input()
    print("AC" if solve(S) else "WA")
    return

if __name__ == '__main__':
    main()
