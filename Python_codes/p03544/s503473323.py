N=int(input())

now = 1
last = 2

for i in range(N):
	now, last = last + now, now
	
print(last)