import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    a, b, c = MI()
    if a <= c and c <= b:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()