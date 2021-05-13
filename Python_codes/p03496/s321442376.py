n = int(input())
a = [int(i) for i in input().split()]
num,num2 = 0,0
for i in range(n):
	if abs(a[i])>abs(num): num,num2=a[i],i
print(2*n-2)
for i in range(n):
	if i!=num2: print(num2+1,i+1)
if num<0:
	for i in range(n-1,0,-1): print(i+1,i)
else:
	for i in range(n-1): print(i+1,i+2)