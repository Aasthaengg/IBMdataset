import bisect

N, K = map(int, input().split())
h_list = list(map(int, input().split()))

h_list = sorted(h_list)

print(N - bisect.bisect_left(h_list, K))