import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))

    max_a = max(A)
    min_a = min(A)

    max_i = A.index(max_a)
    min_i = A.index(min_a)

    ans = []
    if abs(max_a) >= abs(min_a):
        while A[0] < max_a:
            A[0] += max_a
            ans.append([max_i, 0])

        for i in range(N-1):
            while A[i+1] < A[i]:
                A[i+1] += A[i]
                ans.append([i, i+1])
    else:
        while A[N-1] > min_a:
            A[N-1] += min_a
            ans.append([min_i, N-1])

        for i in range(N-1, 0, -1):
            while A[i-1] > A[i]:
                A[i-1] += A[i]
                ans.append([i, i-1])

    print(len(ans))
    for a in ans:
        print(a[0]+1, a[1]+1)


if __name__ == '__main__':
    main()
