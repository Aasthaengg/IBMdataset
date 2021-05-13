import sys
def input():return sys.stdin.readline().strip()

def main():
    N, H = map(int, input().split())
    info = [tuple(map(int, input().split())) for _ in range(N)]
    A_MAX = max(a for a, _ in info)
    Bs = [b for _, b in info if b > A_MAX]

    Bs.sort(reverse=True)
    ans = 0
    for b in Bs:
        if H <= 0:
            break
        ans += 1
        H -= b

    if H > 0:
        ans += (H + A_MAX-1)//A_MAX
    print(ans)

if __name__ == "__main__":
    main()