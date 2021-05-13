n = int(input())
a, b = map(int, input().split())
p = [int(i) for i in input().split()]

p1 = []
p2 = []
p3 = []

for i in p :
	if a >= i:
		p1.append(i)
	elif a+1 <= i <= b:
		p2.append(i)
	elif b+1 <= i:
		p3.append(i)

print(min(len(p1), len(p2), len(p3)))