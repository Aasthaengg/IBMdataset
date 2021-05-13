import sys

def solve():
    input = sys.stdin.readline
    A, B, C = map(int, input().split())
    count = 0
    while count < C:
        if B >= A:
            count += 1
            B -= A
        else: break
    print(count)

    return 0

if __name__ == "__main__":
    solve()