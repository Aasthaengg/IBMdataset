N = int(input())
seq = [i for i in range(1,N+1)]
count = 0
for t in range(0,N):
	if seq[t]%3 != 0 and seq[t]%5 != 0:
		count += seq[t]
print(count)