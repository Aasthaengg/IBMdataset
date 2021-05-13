import sys
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]
    p.sort()
    print(sum(p) - p[-1] // 2)





if __name__ == "__main__":
    main()
