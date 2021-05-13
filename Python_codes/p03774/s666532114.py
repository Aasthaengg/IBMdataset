n, m= map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]
ans = [0] * n
for i,ablist in enumerate(ab):
    mindist = 4 * (10**8)+1
    for j,cdlist in enumerate(cd):
        dist = abs(ablist[0]-cdlist[0])+abs(ablist[1]-cdlist[1])
        if dist < mindist:
            mindist = dist
            ans[i] = j+1
for i in range(n):
	print(ans[i])