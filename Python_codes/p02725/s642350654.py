# coding: utf-8

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))

    tmp1 = A[0] + K - A[-1]
    tmp2 = max([A[i] - A[i-1] for i in range(1, N)])

    print(K - max(tmp1, tmp2))


if __name__ == "__main__":
    main()
