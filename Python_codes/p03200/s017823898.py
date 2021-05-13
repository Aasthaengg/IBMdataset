s = input()

w = []
for i in range(len(s)):
	if s[i] == "W":
		w.append(i)
res = 0

for i in range(len(w)):
	res += w[i] - i
print (res)