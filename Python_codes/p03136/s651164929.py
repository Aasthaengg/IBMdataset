def main():
    N = int(input())
    L = list(map(int,input().split()))
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += L[j]
        sum = sum - L[i]
        if sum <= L[i]:
            return ('No')
    return ('Yes')

print(main())
