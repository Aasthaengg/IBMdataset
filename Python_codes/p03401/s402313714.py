n = int(raw_input())
ais =[0] + map(int,raw_input().split()) + [0]
skip = -float('inf')
cumul = 0
res  = []
for i in range(1,len(ais)-1):
	val = abs(ais[i] - ais[i-1])
	skip = -abs(ais[i] - ais[i-1]) - abs(ais[i+1] - ais[i]) + abs(ais[i+1] - ais[i-1])
	res.append(skip)
	cumul += val
cumul += abs(ais[-1] - ais[-2])
for i in range(len(res)):
	print res[i] + cumul