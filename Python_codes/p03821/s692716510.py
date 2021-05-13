import sys

input = sys.stdin.readline


def main():
    N = int(input())
    AB = [0] * N
    for i in range(N):
        AB[i] = map(int, input().split())

    n_press = 0
    for A, B in reversed(AB):
        r = (A + n_press) % B
        n_press += B - r if r > 0 else 0

    ans = n_press
    print(ans)


if __name__ == "__main__":
    main()
