n = int(raw_input())
count,res,ais,i = 0,0, map(int , raw_input().split()),0
while(i < n+1):
	if (ais[i] if i < n else -1) != i + 1:
		res += (count + 1)/2# + 1
		count = 0
	else: count +=1
	i+=1
print res