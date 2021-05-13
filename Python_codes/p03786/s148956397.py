from itertools import accumulate

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    CUSUM = tuple(accumulate(A))

    sub = 0
    for i in range(N-1):
        if CUSUM[i]*2 < A[i+1]:
            sub = i+1
    print(N-sub)
    
if __name__ == "__main__":
    main()