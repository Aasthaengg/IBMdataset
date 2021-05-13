import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n = int(input())

    n26 = 1
    keta = 0
    while n > 0:
        n26 *= 26
        n -= n26
        keta += 1
    n = n + n26 - 1
    r = []
    for i1 in range(keta):
        t1 = n % 26
        r.append(chr(t1 + 97))
        n = n // 26
    print("".join(r[::-1]))

if __name__ == '__main__':
    main()