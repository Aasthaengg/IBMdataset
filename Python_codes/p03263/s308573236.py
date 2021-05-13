
def main():
    H, W = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(H)]
    A = [[i, j, k] for i, a in enumerate(A) for j, k in enumerate(a)]
    for i in range(W, len(A), 2 * W):
        A[i: i + W] = A[i + W - 1:i - 1:-1]
    i = 0
    ans = []
    count = 0
    while i < len(A):

        if A[i][2] % 2 != 0:
            j = 1
            while i + j < len(A):
                if A[i + j][2] % 2 != 0:
                    for k in range(i, i + j):
                        ans.append([A[k][0], A[k][1], A[k + 1][0], A[k + 1][1]])
                        count += 1
                    i += j
                    break
                j += 1
            else:
                break
        else:
            pass
        i += 1
    print(count)
    for a in ans:
        print(' '.join(list(map(lambda x: str(x + 1), a))))

if __name__ == '__main__':
    main()
