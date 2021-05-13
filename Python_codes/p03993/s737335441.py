N = int(input())
l = tuple(map(int, input().split()))
cnt = 0
for i in range(N):
	if l[l[i]-1] == i+1:
		cnt += 1
print(cnt//2)