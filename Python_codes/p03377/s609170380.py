#!/usr/bin/env python3

def main():
    a, b, x = map(int, input().split())
    print("YES" if a <= x <= a + b else "NO")

if __name__ == "__main__":
    main()
