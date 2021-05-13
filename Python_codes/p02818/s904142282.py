import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    a, b, k = map(int, input().split())
    if a >= 1:
        if k > a:
            k = k - a
            a = 0
        else:
            a = a - k
            k = 0
    if b >= 1:
        if k > b:
            b = 0
        else:
            b = b - k
    print(a, b)

if __name__ == '__main__':
    main()