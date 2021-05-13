N = input()
n = map(int,raw_input().split(' '))
c = 0
for i in range(N-1):
	mini = i
	for j in range(i+1,N):
		if n[mini] > n[j]:
			mini = j
	if mini != i:
		temp = n[i]
		n[i] = n[mini]
		n[mini] = temp
		c+=1
print " ".join(str(i) for i in n)
print c