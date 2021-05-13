MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)

def main():
    X,Y = map(int,input().split())
    ans = 0
    power = 1
    while power*X <= Y:
        ans += 1
        power *= 2
    print(ans)
if __name__ == '__main__':
    main()