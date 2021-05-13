k = int(input())
n  =1000
t  =[]

for i in range(1,11):
	if n*i-k>=0:
		t.append(n*i-k)

print(min(t))