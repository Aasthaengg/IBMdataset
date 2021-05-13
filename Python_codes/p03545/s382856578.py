correct = []
def dfs(i, s, stack):
	if i == 4:

		if eval(''.join(stack)) == 7:
			correct.append(''.join(stack) + '=7')
			return True
		else:
			return False

	if dfs(i+1, s,stack + ['+', s[i]]): return True
	if dfs(i+1, s,stack + ['-', s[i]]): return True
	return False
s = raw_input()
dfs(1, s, [s[0]])
print correct[0]