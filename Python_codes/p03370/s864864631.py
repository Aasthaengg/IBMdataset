n,x = map(int,input().split())
number = []
for i in range(n):
	number.append(int(input()))
x -= sum(number)
print(n + x // min(number))