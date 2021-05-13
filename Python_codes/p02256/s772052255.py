def euclideanAlg(n, m):
    r = n % m
    if r == 0:
        return m
    else:
        return euclideanAlg(m, r)

if __name__ == "__main__":
    A = map(int, raw_input().split())
    print euclideanAlg(A[0], A[1])