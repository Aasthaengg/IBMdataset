#!/usr/bin/env python3

def main():
    k = int(input())
    n = 50
    a = list(range(n))
    for i in range(n):
        a[i] += k // n
    for i in range(k % n):
        a[n - i - 1] += 1
    print(n)
    print(" ".join(str(x) for x in a))

if __name__ == "__main__":
    main()
