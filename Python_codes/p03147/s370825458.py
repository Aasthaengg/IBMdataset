n = int(input())
h = list(map(int,input().split()))
ans,cnt = [0]*n,0
h.append(1)
ans.append(1)
while(h!=ans):
	for i in range(n):
		if h[i] > 0:
			h[i] -= 1
			if h[i+1] == 0:
				break
	cnt += 1
print(cnt)