import sys
import bisect
sys.setrecursionlimit(1 << 25)
read = sys.stdin.readline

def main():
    n,t = map(int,read().split())
    li = list(map(int,read().split()))
    now = -1e18
    ans = 0
    for ti in li:
        if now < 0:
            now = ti
        else:
            ans += min(t,ti-now)
            now = ti
        
    print(ans+t)

if __name__ == '__main__':
    main()
