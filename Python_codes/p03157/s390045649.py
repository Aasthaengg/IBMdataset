import sys
sys.setrecursionlimit(10000000)
H, W = map(int, input().split())
S = [input() for _ in range(H)]
seen = [[0]*W for _ in range(H)]


def rec(h,w,seen):
	if S[h][w] == '.':
		res = [1, 0]
	else:
		res = [0, 1]
	dh = [-1, 1, 0, 0]
	dw = [0, 0, -1, 1] 
	seen[h][w] = 1
	for i in range(4):
		nh = h+dh[i]
		nw = w+dw[i]
		if 0 <= nh <= H-1 and 0 <= nw <= W-1:
			if seen[nh][nw] == 0 and S[nh][nw] != S[h][w]:
				r0, r1 = rec(nh, nw, seen)
				res[0] += r0
				res[1] += r1
					
	return res

ans = 0
for h in range(H):
	for w in range(W):
		if seen[h][w] != 1:
			t0, t1 = rec(h, w, seen)
			ans += t0 * t1
print(ans)
