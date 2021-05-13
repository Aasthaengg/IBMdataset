import sys
def input(): return sys.stdin.readline().strip()

def main():
    N = int(input())
    K = int(input())
    ans = 10**18
    for i in range(1 << N):
        val = 1
        for j in range(N):
            if i & (1 << j):
                val *= 2
            else:
                val += K
        ans = min(ans, val)
    print(ans)


if __name__ == "__main__":
    main()
