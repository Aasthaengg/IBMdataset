import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    large_p = 10 ** 9 + 7
    n = int(input())
    r = 1
    for i1 in range(1, n + 1):
        r = (r * i1) % large_p

    print(r)

if __name__ == '__main__':
    main()
