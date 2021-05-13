N=int(input())
array=[int(x) for x in input().split()]
XOR=0
for i in array:
	XOR=XOR^i
print(*[XOR^x for x in array])