
def main():
    N = int(input())
    A, B = [], []
    for _ in range(N):
        a, b = map(int,input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()

    if N % 2 != 0:
        ma = A[N//2]    
        mb = B[N//2]
        print(mb - ma + 1)
    else:
        ma = A[N//2-1] + A[N//2] # 中央値は/2がいるが、この場合は分子が分かればよい
        mb = B[N//2-1] + B[N//2]
        print(mb - ma + 1)


if __name__ == "__main__":
    main()

