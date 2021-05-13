n = int(input())
cnt = 0
for i in range(n//2):
	if (i+1)+ (i+1) == n:
		continue
	cnt +=1
print (cnt)