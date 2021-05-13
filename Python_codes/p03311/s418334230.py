import statistics
def main():
    N, A = int(input()), list(map(int, input().split()))
    for i in range(N):
        A[i] -= i + 1
    m = int(statistics.median(A))
    a, b = m, m + 1
    c, d = 0, 0
    for el in A:
        c += abs(el-a)
        d += abs(el-b)
    print(min(c, d))
main()