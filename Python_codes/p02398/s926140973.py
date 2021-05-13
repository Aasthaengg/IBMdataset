a, b, c = map(int, input().split())
i=a
j=0

while a <= i <= b:
	if c % i == 0:
		j = j+1
	i = i+1
	
print(j)