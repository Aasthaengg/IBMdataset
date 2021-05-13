'''input
0
'''
k = input()
arr = []
zz = k%50
for i in range(50-zz):
	arr.append(49-zz)
for i in range(zz):
	arr.append(50)
zzz = k//50
arr = [arr[i]+zzz for i in range(50)]
print 50
for i in range(50):
	print arr[i],
