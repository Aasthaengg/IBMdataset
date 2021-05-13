import sys
input = sys.stdin.readline

def main():
    N, A, B = map(int, input().split())
    x = list(map(int, input().split()))

    ans = 0
    for i in range(N-1):
        tmp_a = (x[i+1] - x[i]) * A
        if tmp_a <= B:
            ans += tmp_a
        else:
            ans += B
    print(ans)


if __name__ == "__main__":
    main()