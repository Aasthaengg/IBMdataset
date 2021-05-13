import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    a, b = map(int, input().split())
    r = 0
    for i1 in range(a, b + 1):
        stri1 = str(i1)
        r += stri1 == stri1[::-1]

    print(r)

if __name__ == '__main__':
    main()
