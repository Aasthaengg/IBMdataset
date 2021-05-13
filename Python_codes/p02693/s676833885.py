def solve():
    K = int(input())
    A,B = [int(i) for i in input().split()]
    qA,rA = divmod(A, K)
    qB,rB = divmod(B, K)
    if rA == 0 or rB == 0:
        print("OK")
    elif qB - qA > 0:
        print("OK")
    else:
        print("NG")

if __name__ == "__main__":
    solve()