MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)

def main():
    a = list(map(int,input().split()))
    a.sort()
    ans = a[0] + a[1] + a[2] * 10
    print(ans)
if __name__ == '__main__':
    main()