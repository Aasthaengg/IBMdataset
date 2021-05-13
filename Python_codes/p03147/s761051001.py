import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    h = list(map(int, input().split()))
    arr = [h[0]] + [0] * (n - 1)
    ans = 0
    for i in range(1, n):
        arr[i] = h[i] - h[i-1]
    for i in range(n):
        if arr[i] > 0:
            ans += arr[i]
    print(ans)
        
if __name__ == '__main__':
    main()