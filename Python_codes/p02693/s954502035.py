import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    k = int(input())
    a, b = map(int, input().split())
    for i1 in range(a, b + 1):
        if i1 % k == 0:
            print('OK')
            sys.exit()
    print('NG')

if __name__ == '__main__':
    main()
