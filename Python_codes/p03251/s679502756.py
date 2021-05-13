import sys
def input(): return sys.stdin.readline().strip()


def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x.sort()
    y.sort()
    if x[-1] < y[0]:
        war = True
        for z in range(x[-1] + 1, y[0] + 1):
            if X < z <= Y:
                war = False
                break
        if war: print("War")
        else: print("No War")
    else:
        print("War")


if __name__ == "__main__":
    main()
