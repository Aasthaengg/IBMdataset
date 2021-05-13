def actual(N, A):
    return max(A) - min(A)

N = int(input())
A = list(map(int, input().split()))

print(actual(N, A))
