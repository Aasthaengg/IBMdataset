def resolve():
    n = int(input())
    B = list(map(int, input().split()))
    total = B[0]
    for i in range(n-2):
        total += min(B[i], B[i+1])
    total += B[-1]
    print(total)
resolve()