N = int(input())
xu = [list(map(str,input().split())) for i in range(N)]
sum = 0
for j in range(N):
	if xu[j][1] == 'JPY':
		sum += float(xu[j][0])
	else:
		sum += float(xu[j][0])*380000
print(sum)