n = int(input())

cnt = [0] * 10001

for i in range(1, 100):
	for j in range(1, 100):
		for k in range(1, 100):
			x = i*i + j*j + k*k + i*j + j*k + i*k
			if(x <= 10000):
				cnt[x]+=1

for i in range(1, n+1):
	print(cnt[i])