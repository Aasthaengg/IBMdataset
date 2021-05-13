n=int(raw_input())
a={}
for i in range(n):
	inst,key=raw_input().split()
	if inst=='insert': 
		a.update({key:i})
	elif inst=='find': 
		if a.has_key(key)==True:
			 print 'yes'
		else:print 'no'