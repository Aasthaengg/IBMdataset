# A - Dividing a String
def count_substrings(first_substring):

	arr = [first_substring]
	i = len(first_substring)

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

	return len(arr)


S = input()

ans1 = count_substrings(S[:1])
ans2 = count_substrings(S[:2])

print(max(ans1, ans2))