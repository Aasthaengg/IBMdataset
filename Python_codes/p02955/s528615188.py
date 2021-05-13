n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
candidate=set()
result=0
x=1
while x**2<=(sum(a)+1):
	if sum(a)%x==0:
		candidate.add(x)
		candidate.add(int(sum(a)/x))
	x+=1
# print(candidate)
for i in candidate:
	b=[0]*len(a)
	for j in range(len(a)):
		b[j]=int(a[j]%i)
	b.sort()
	if sum(b[:int(len(b)-sum(b)/i)])<=k:
		result=max(result,i)

	# need=0
	# need+=sum(b)/i
	# if need<=k:
print(result)

