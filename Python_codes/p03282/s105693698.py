S = input()
K = int(input())

ans = 1
for i in S:
	if i != '1':
		ans = i
		break
	if K==1:
		ans = i
		break
	K-=1
print(ans)