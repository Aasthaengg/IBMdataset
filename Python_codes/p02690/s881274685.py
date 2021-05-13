import sys

def solve():
    input = sys.stdin.readline
    X = int(input())
    fin = False
    for i in range(-1000, 1001):
        for j in range(-1000, 1001):
            if pow(i, 5) - pow(j, 5) == X:
                print(i, j)
                fin = True
                break
        if fin: break
    else: print(-1)

    return 0

if __name__ == "__main__":
    solve()