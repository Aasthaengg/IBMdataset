import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n = I()
    d = [0]*(n+1)
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            d[j] += 1
    ans = 0
    for i in range(n+1):
        if i%2 and d[i] == 8:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()