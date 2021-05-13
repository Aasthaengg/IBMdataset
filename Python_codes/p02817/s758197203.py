import sys
input = sys.stdin.readline
MOD = 10**9 + 7
INF = float('INF')

def main():
    s, t = list(map(str,input().split()))
    print(t+s)

if __name__ == '__main__':
    main()