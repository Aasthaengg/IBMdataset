def main():
    n, x = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = [min(A[0], x), ]
    for i in range(n - 1):
        if B[i] + A[i + 1] > x:
            B.append(x - B[i])
        else:
            B.append(A[i + 1])
    ans = sum([a - b for a, b in zip(A, B)])
    print(ans)

if __name__ == '__main__':
    main()
