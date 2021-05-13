N = int(input())
a = list(map(int,input().split()))
b = [0]
b += a
cnt = 0
for i in range(1,N+1):
	if i == b[b[i]]:
		cnt += 1
print(cnt // 2)