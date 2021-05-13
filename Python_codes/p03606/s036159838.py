N=int(input())

Seat = [list(map(int,input().split())) for _ in range(N)]

ans = 0
for s in Seat:
	ans += s[1] - s[0] + 1
print(ans)