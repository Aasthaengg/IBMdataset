N=int(input())
array=[int(x) for x in input().split()]
diff=0
for i in range(1,N):
	if array[i]<array[i-1]:
		diff+=array[i-1]-array[i]
		array[i]+=array[i-1]-array[i]
print(diff)