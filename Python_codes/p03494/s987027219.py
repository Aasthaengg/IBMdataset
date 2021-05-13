n = int(raw_input())
ais = map(int, raw_input().split())
c = 0
while(all([(ai % 2 ==0) for ai in ais ])):
	ais = [ai/2 for ai in ais]	
	c +=1
print c