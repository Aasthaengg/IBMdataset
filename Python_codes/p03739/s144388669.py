n = int(input())
arr = list(map(int , input().split()))
cur = 0
a = 0
b = 0
prea=0
preb=0
resa = 0
resb =0
# check independently even prefix having negative sum and odd prefix having positive sum
for i in range(0 , n):
	prea = prea+arr[i]
	if (i% 2 ==0 and prea<=0):
		resa = resa-prea+1
		prea=1
	if i%2 ==1 and prea>=0:
		resa = resa+prea+1
		prea=-1
# check independently even prefix having positive sum and odd prefix having negative sum
for i in range(0 , n):
	preb = preb+arr[i]
	if (i%2==1 and preb<=0):
		resb = resb+(-preb+1)
		preb=1
	if i%2 ==0 and preb>=0:
		resb =resb+ preb+1
		preb=-1
# find minimum of the two
print(min(resa , resb))