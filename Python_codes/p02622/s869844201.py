s = input()
t = input()
s_line = list(s)
t_line = list(t)
count=0
for a,b in zip(s_line,t_line):
	if a!=b: count +=1
print(count)