import sys
def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N = Z()
    i = 0
    print(i, flush=True)
    s = input()

    f = s
    first, last = 0, N

    while s != 'Vacant':
        i = (first + last)//2
        print(i, flush=True)
        s = input()
        if s == 'Vacant': break
        if (i%2 == 0 and f == s) or (i%2 == 1 and f != s): first = i
        else: last = i
    return

if __name__ == '__main__':
    main()
    sys.exit(0)
