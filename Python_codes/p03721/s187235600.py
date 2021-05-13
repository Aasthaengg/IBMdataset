n , k = map(int , input().split())
arr = []
for i in range(0 , n):
	arr.append(list(map(int , input().split())))
# sort according the element of the array first value
arr.sort()
cur =0
# continue to add the frequency of every element in increasing order upto k
for i in range(0 , n):
	if cur + arr[i][1]<k:
		cur = cur+arr[i][1]
	else:
		print(arr[i][0])
		exit()