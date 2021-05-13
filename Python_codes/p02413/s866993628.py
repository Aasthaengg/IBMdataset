r, c = map(int, input().split()) # r = 4, c = 5
ss = [list(map(int, input().split())) for row in range(r)] 
for line in ss:
	line.append(sum(line))

sum_line = [0 for i in range(c + 1)] # ?????????1????????§??????.
for line in ss:
	for i in range(c + 1):
		sum_line[i] += line[i]
ss.append(sum_line)

for i in range(r + 1):
	print(' '.join(map(str, ss[i])))