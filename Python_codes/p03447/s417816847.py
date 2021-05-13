import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    x = int(input())
    a = int(input())
    b = int(input())
    print((x-a)%b)

if __name__ == '__main__':
    main()