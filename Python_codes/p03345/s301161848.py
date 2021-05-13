import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    A,B,C,K = map(int,input().split())
    if K%2 == 0:
        ans = A - B
    else:
        ans = B - A
    if abs(ans) > 1000000000000000000:
        ans = 'Unfair'
    print(ans)
if __name__ == '__main__':
    main()