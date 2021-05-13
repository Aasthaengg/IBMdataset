n = int(input())
x = input().split()
a, v = x[0], x[1]
res=""
j=0
k=0
for i in range(2*n):
	if i%2==0:
		res +=a[j]
		j +=1
	else:
		res +=v[k]
		k+=1
print(res)