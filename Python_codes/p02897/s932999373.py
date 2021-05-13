import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    if n % 2 == 0:
        print(n/2/n)
    else:
        print(((n//2)+1)/n)

if __name__ == '__main__':
    main()