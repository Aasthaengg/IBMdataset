# yahoo-procon2019-qualB - Path
import sys
input = sys.stdin.readline

def main():
    C = [0] * 4
    for _ in range(3):
        a, b = map(int, input().split())
        C[a - 1] += 1
        C[b - 1] += 1
    print("YES" if set(C) == {1, 2} else "NO")


if __name__ == "__main__":
    main()