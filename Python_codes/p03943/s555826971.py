Cnd = list(map(int,input().split()))
Cnd = sorted(Cnd)
result = 'No'
if Cnd[0]==Cnd[1]+Cnd[2]:
	result ='Yes'
if Cnd[0]+Cnd[1]==Cnd[2]:
	result ='Yes'
print(result)