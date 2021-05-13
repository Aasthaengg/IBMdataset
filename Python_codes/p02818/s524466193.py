def solve():
    A,B,K = [int(i) for i in input().split()]
    if K >= A:
        B = max(0, B-(K-A))
        A = 0
    else:
        A -= K
    print(A, B)

if __name__ == "__main__":
    solve()