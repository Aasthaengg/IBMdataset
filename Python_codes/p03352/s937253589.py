def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1 )) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append((i, cnt))
    if temp != 1:
        arr.append((temp, 1))
    if arr == []:
        arr.append((n, 1))
    return arr

def solve():
    X = int(input())
    for i in range(X, 0, -1):
        F = factorization(i)
        mi = min(f[1] for f in F)
        if mi > 1 and all([f[1] % mi == 0 for f in F]):
            print(i)
            exit()
    print(1)

if __name__ == "__main__":
    solve()