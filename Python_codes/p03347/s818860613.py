# AGC024C - Sequence Growing Easy
def main():
    N, *A = map(int, open(0))
    if A[0]:  # can't increment A_0
        print(-1)
        return
    A.append(0)
    ans, B = 0, A[::-1]
    for i, j in zip(B, B[1:]):  # check from the last
        if i > j + 1:  # increment from left one must be 0 or 1
            print(-1)
            return
        if j >= i:  # left one is an end of subsequence
            ans += j
    print(ans)


if __name__ == "__main__":
    main()