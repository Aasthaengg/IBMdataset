import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    a, b = map(int, input().split())
    diff = b - a
    high = sum([i for i in range(diff)])
    print(high - a)

if __name__ == '__main__':
    main()
