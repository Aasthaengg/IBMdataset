import sys
def input(): return sys.stdin.readline().strip()


def main():
    N, T = map(int, input().split())
    ans = 10**10
    for _ in range(N):
        c, t = map(int, input().split())
        if t <= T: ans = min(ans, c)
    if ans == 10**10: print("TLE")
    else: print(ans)



if __name__ == "__main__":
    main()
