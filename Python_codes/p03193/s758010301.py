N, H, W = input().split()
N = int(N)
H = int(H)
W = int(W)
cnt = 0

for i in range(N):
	sozai_h, sozai_w = input().split()
	sozai_h = int(sozai_h)
	sozai_w = int(sozai_w)
	if sozai_h >= H and sozai_w >= W:
		cnt += 1
print (cnt)