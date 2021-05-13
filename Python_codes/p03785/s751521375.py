import sys
input = sys.stdin.readline

# A - Airport Bus
N, C, K = map(int, input().split())
times = []

for i in range(N):
	T = int(input())
	t = [T, T + K]
	times.append(t)

times.sort(key=lambda x: x[1])

ans = 0
count = 0
departure_time = 0

for t in times:
	if count == 0:
		departure_time = t[1]
		count = 1
	elif count < C:
		if t[0] <= departure_time:
			count += 1
		else:
			ans += 1
			departure_time = t[1]
			count = 1
	elif count == C:
		ans += 1
		departure_time = t[1]
		count = 1

if count <= C:
	ans += 1

print(ans)