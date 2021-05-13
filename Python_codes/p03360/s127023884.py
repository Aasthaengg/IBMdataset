A = sorted(map(int, input().split()))
k = int(input())

A[-1] *= 2**k

print(sum(A))
