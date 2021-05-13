n,x = map(int, raw_input().split(' '))
ais = map(int, raw_input().split(' '))
count,cur,i = 1,0, 0
res = []
while(i < len(ais)):
	cur += ais[i]
	if cur <= x:
		count+=1
	else:
		break

	i +=1
print count
#print len([e for e in res if e <= x])