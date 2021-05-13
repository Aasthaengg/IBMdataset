N = int(input())
song = ["a"] * N
time = [0] * N
for i in range(N):
	s, t = input().split()
	song[i] = s
	time[i] = int(t)
X = input()

idx = 0
for i in range(N):
	if X == song[i]:
		idx = i
		break

ans = 0
for i in range(idx+1, N):
	ans += time[i]

print(ans)