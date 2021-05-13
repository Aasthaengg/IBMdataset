s = list(input())

all = len(s)
g = s.count('g')
p = s.count('p')

top = g-p

if all%2 == 1:
	deer = 1
	top += 1
	top //= 2
elif all%2 == 0:
	deer = 0
	top //= 2 
print(top - deer)