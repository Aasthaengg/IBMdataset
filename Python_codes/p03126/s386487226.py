import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, m = map(int, input().split())
    foods = [0] * m
    ans = 0
    for _ in range(n):
        k = list(map(int, input().split()))
        for i in range(1, k[0]+1):
            foods[k[i]-1] += 1
    for i in range(m):
        if foods[i] == n:
            ans += 1
    print(ans)
        
if __name__ == '__main__':
    main()