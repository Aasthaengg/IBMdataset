#!python3

# input
N, K = list(map(int, input().split()))


def main():
    if N % K == 0:
        ans = 0
    else:
        ans = 1
    print(ans)
    


if __name__ == "__main__":
    main()
