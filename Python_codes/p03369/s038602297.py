#!/usr/bin/env python3

def main():
    s = input()
    res = 700
    for c in s:
        if c == "o":
            res += 100
    print(res)

if __name__ == "__main__":
    main()
