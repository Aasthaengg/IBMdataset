import sys

input = sys.stdin.readline


def main():
    R, G, B, N = map(int, input().split())

    ans = 0
    for r in range(N // R + 1):
        gGbB = N - r * R
        for g in range(gGbB // G + 1):
            bB = gGbB - g * G
            if bB % B == 0:
                ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()
