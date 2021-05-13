n,ais,cumul,res =int(raw_input()),[0] + map(int,raw_input().split()) + [0],0,[]
for i in range(1,len(ais)):
	if i < len(ais) -1: res.append(-abs(ais[i] - ais[i-1]) - abs(ais[i+1] - ais[i]) + abs(ais[i+1] - ais[i-1]))
	cumul += abs(ais[i] - ais[i-1])
for v in res: print v + cumul