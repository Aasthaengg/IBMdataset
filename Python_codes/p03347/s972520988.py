def is_possible(A):
    if A[0] != 0:
        return False
    for i in range(1, len(A)):
        if A[i-1] < A[i] - 1:
            return False
    return True

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    if not is_possible(A):
        print(-1)
        return
    ans = 0
    i = N-1
    while i >= 0:
        if A[i] > 0:
            x = A[i]
            ans += x
            while i >= 0 and x > 0 and A[i] == x:
                i -= 1
                x -= 1
        else:
            i -= 1
    print(ans)

if __name__ == "__main__":
    main()
