def actual(n, A):
    return 1 / sum([(1 / x) for x in A])

n = int(input())
A = list(map(int, input().split()))

print(actual(n, A))
