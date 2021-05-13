n = int(input())
a = list(map(int, input().split()))

cnt = 0
chk = [False for i in range(n)]
for i in range(n):
	if chk[i]:
		continue
	chk[i] = True
	if i+1 == a[a[i]-1]:
		chk[a[i]-1] = True
		cnt += 1
print (cnt)