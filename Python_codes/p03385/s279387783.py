#!/usr/bin/env python3

def main():
    s = input()
    if len(set(s)) == 3:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
