import sys

r,c = map(int,raw_input().split())
table_list = [[0 for i in range(c)]for j in range(r)]
for k in range(r):
	Sum = 0
	table_list[k] = map(int,raw_input().split())
	for l in table_list[k]:
		Sum += l
	table_list[k].append(Sum)
end_list = []
for m in range(c):
	Sum = 0
	for n in range(r):
		Sum += table_list[n][m]
	end_list.append(Sum)
Sum = 0
for o in end_list:
	Sum += o
end_list.append(Sum)
table_list.append(end_list)
for p in range(r+1):
	for q in range(c+1):
			if q==c:
				print '%d' %table_list[p][q]
			else :
				sys.stdout.write(str(table_list[p][q]))
				sys.stdout.write(' ')