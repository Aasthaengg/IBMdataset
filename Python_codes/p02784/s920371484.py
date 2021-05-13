def resolve():
    H, N = list(map(int, input().split()))
    A = list(map(int, input().split()))
    print("Yes" if sum(A) >= H else "No")

if '__main__' == __name__:
    resolve()