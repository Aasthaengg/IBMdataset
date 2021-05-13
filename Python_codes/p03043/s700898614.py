import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        x = 0
        while i < k:
            x += 1
            i *= 2
        ans += (1 / n) * (1 / 2)**x
    print(ans)
    
if __name__ == '__main__':
    main()