#!/usr/bin/env python3

def main():
    n = int(input())
    s1 = input()
    s2 = input()
    i = 0
    res = 1
    while i < n:
        if i == 0:
            if s1[i] == s2[i]:
                res *= 3
                i += 1
                pretwo = False
            else:
                res *= 6
                i += 2
                pretwo = True
        else:
            if s1[i] == s2[i]:
                res *= (1 if pretwo else 2)
                i += 1
                pretwo = False
            else:
                res *= (3 if pretwo else 2)
                i += 2
                pretwo = True
    print(res % (10 ** 9 + 7))

if __name__ == "__main__":
    main()
