MOD = 10 ** 9 + 7
def main():
    N, K = (int(_) for _ in input().split())
    A = [int(_) for _ in input().split()]

    R, L = [], []
    for i in range(N):
        cr = cl = 0
        for j in range(N):
            if i == j: continue
            if A[i] > A[j]:
                if i > j: cl += 1
                if i < j: cr += 1
        R.append(cr)
        L.append(cl)

    output = 0
    for i in range(N):
        output += (K*R[i] + K*(K-1)*(R[i]+L[i])//2)
        output %= MOD
    print(output)
    return

if __name__ == '__main__':
    main()
