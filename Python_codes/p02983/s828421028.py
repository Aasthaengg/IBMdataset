L,R=[int(x) for x in input().split()]
R=min(R,L+2018)
numbers=[x%2019 for x in range(L,R+1)]
length=len(numbers)
minimum=[]
for i in range(length):
	for j in range(i+1,length):
		minimum.append((numbers[i]*numbers[j])%2019)
print(min(minimum))