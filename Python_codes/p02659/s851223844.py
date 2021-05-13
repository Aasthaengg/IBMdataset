import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    a, b = input().split()

    a = int(a)
    b = b.replace('.','')
    b = int(b)
    r = (a * b) // 100
    print(r)

if __name__ == '__main__':
    main()
