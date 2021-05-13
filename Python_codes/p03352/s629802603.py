#!/usr/bin/env python3

def solve(x):
    if x == 1:
        return 1
    f = 2
    l = [1]
    while f * f <= x:
        d = f
        while d <= x:
            l.append(d)
            d *= f
        f += 1
    return max(l)



def main():
    X = int(input())
    print(solve(X))
    return

if __name__ == '__main__':
    main()
