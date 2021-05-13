N = int(input())

A = []

for i in range (0, N):
	A.append(list(map(int, input().split())))

def Sort(F): 
  
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of  
    # sublist lambda has been used 
    F.sort(key = lambda x: x[1]) 
    return F 

A = Sort(A)

date = 0

for i in range (0, N):
	if date + A[i][0] > A[i][1]:
		print('No')
		exit()
	else:
		date+=A[i][0]

print('Yes')