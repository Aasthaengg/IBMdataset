import sys
input = sys.stdin.readline

# B - Bitter Alchemy
N, X = map(int, input().split())
m = []

for i in range(N):
	m.append(int(input()))
	
ans = N
remaining = X - sum(m)

m.sort()

ans += remaining // m[0]

print(ans)