n,x = map(int, raw_input().split(' '))
ais = map(int, raw_input().split(' '))
count,cur,i = 0,0, 0
res = [cur]
while(i < len(ais)):
	cur += ais[i]
	res.append(cur)
	i +=1

print len([e for e in res if e <= x])