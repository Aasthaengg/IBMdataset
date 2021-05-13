# A - Dividing a String
S = input()

arr = [S[0]]
i = 1

while i < len(S):
	s = S[i]
	
	if s == arr[-1]:
		if i + 1 < len(S):
			i += 1
			s += S[i]
		else:
			arr[-1] += s
			break
	
	arr.append(s)
	i += 1

print(len(arr))