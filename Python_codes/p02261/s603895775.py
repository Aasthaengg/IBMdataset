N = input()
n = list(raw_input().split())
b = list(n)
for i in range(N-1):
	for j in range(N-i-1):
		if b[j][1] > b[j+1][1]:
			w = b[j]
			b[j] = b[j+1]
			b[j+1] = w
print " ".join(b[i] for i in range(N))
print "Stable"
for i in range(N-1):
	m = i
	for j in range(i+1,N):
		if n[m][1] > n[j][1]:
			m = j
	if m != i:
		w = n[i]
		n[i] = n[m]
		n[m] = w
print " ".join(n[i] for i in range(N))
if b == n:
	print "Stable"
else:
	print "Not stable"