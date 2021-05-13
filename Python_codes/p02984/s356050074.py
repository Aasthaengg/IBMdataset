import sys

readline = sys.stdin.readline

def main():
    N = int(readline())
    A = list(map(int, readline().split()))

    ans = []
    a = (sum(A[::2]) - sum(A[1::2]))//2
    ans.append(2*a)
    for i in range(N-1):
        b = A[i] - a
        ans.append(2*b)
        a = b

    print(*ans)

if __name__ == "__main__":
    main()
