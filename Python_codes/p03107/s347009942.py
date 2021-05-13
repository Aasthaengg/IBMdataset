import collections

s = raw_input()
stack = collections.deque([])
i = 0
j = 0
while(j < len(s)):
	while(j < len(s) and s[i] == s[j]): j += 1	
	stack.append(j-i)
	i = j
n = len(s)
while(len(stack) > 1) :
	v = stack.pop()
	u = stack.pop()
	if v > u: 
		if stack:
			stack[-1] += v-u
		else:
			stack.append(v-u)
	elif v < u: stack.append( u - v)

print n - (stack[-1] if stack else 0)