
numbers = []
n = int(raw_input())

S = raw_input()

b = S.split(" ")
s = S.split(" ")

for i in range(n):
    for j in  range(n - 1, i, -1):
        if int(b[j][-1]) < int(b[j - 1][-1]):
        	b[j], b[j - 1] = b[j - 1], b[j]
print ' '.join(b)
print "Stable"

for i in range(n):
	minj = i
	for j in range(i, n):
		if int(s[j][-1]) < int(s[minj][-1]):
			minj = j
	s[i], s[minj] = s[minj], s[i]

print ' '.join(s)
flag = 0
for i in range(n):
	if b[i] != s[i]:
		flag = 1
if flag:
	print "Not stable"
else:
	print "Stable"