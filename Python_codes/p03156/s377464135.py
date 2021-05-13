import bisect

N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))

P.sort()

a = bisect.bisect_right(P, A)
b = bisect.bisect_right(P, B)

print(min(a, b - a, N - b))
