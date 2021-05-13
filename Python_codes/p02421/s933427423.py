num = int(input())

t=0
h=0

for i in range(num):
	Ta,Ha = input().split(" ")
	if Ta > Ha:
		t += 3
	elif  Ta < Ha:
		h += 3
	else:
		t += 1
		h += 1
print(t,h)

