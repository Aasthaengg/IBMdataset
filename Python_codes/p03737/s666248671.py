array=input().split()
tobeprinted=[]
for i in range(3):
	tobeprinted.append(array[i][0].upper())
print(*tobeprinted,sep="")