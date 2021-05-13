import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, i = map(int, input().split())
    print(N - i + 1)

if __name__ == '__main__':
    main()
