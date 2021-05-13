import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, T = map(int, input().split())
    ans = 10000
    for _ in range(n):
        c, t = map(int, input().split())
        if t <= T:
            ans = min(ans, c)
    print(ans if ans <= 1000 else 'TLE')
    
if __name__ == '__main__':
    main()
