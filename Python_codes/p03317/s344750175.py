import math
def main():
    N, K = map(int, input().split())
    A = [int(a) for a in input().split()]

    if N == 1:
        print(0)
    elif N <= K:
        print(1)
    else:
        print(1+math.ceil((N-K)/(K-1)))

if __name__ == "__main__":
    main()