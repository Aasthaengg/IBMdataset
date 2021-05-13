data = input()
datas = data.split(' ')

N = int(datas[0])
K = int(datas[1])

if K==1:
	print(0)
else:
	print(N-K)