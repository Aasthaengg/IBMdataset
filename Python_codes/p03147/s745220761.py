import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = h[0]
    for i in range(1, n):
        if h[i] - h[i-1] > 0:
            ans += h[i] - h[i-1]
    print(ans)
        
if __name__ == '__main__':
    main()