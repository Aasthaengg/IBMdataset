N = int(input())						# 5
A = sorted(list( map(int, input().split()) ))	# 1 2 3 4 5 ...(ソート付き)

ANS=[]

a=A[0]
z=A[-1]

s=0
t=0

for i in A[1:-1]:
	if i>=0:
		ANS.append((a,i))
		a = a-i
	else:
		ANS.append((z,i))
		z = z-i


ANS.append((z,a))

print(z-a)
for a in ANS:
	print(*a)

