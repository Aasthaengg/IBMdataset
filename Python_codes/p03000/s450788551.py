from bisect import bisect_right
N, X = map(int, input().split())
L = list(map(int, input().split()))
s = [0] * (N+1)
for i in range(N):
	s[i+1] = s[i] + L[i]
pos = bisect_right(s, X)
print(pos)