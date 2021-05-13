import sys
sys.setrecursionlimit(100000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = sum(a -1 for a in A)
    print(ans)
if __name__ == '__main__':
    main()
