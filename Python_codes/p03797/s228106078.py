import sys
def input(): return sys.stdin.readline().strip()

def main():
    N, M = map(int, input().split())
    if M <= 2 * N:
        print(M // 2)
    else:
        k = (M - 2 * N) // 4
        ans= 0
        for i in range(max(0, k - 4), min(M // 2, k + 4)):
            if (M - 2 * i) <= 2 * (N + i):
                ans = max(ans, (M - 2 * i) // 2)
            else:
                ans = max(ans, N + i)
        print(ans)
    
    

if __name__ == "__main__":
    main()
