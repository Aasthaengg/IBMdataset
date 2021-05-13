import bisect
N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort()

print(N-bisect.bisect_left(H, K))