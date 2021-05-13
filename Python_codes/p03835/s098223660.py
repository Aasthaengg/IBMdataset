import sys

input = sys.stdin.readline

K, S = list(map(int,input().split()))

ans = 0

for i in range(K+1):
	for j in range(K+1):
		if S-K<=i+j<=S:
			ans += 1

print(ans)