K, N = map(int, input().split())
A = list(map(int, input().split()))

d = [a1 - a2 for (a1, a2) in zip(A[1:], A[:-1])]
d.append(A[0] + K - A[-1])

print(sum(d) - max(d))