n, t = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

max_list = []
tmp = A[0]
max_tmp = -1011100011
for num in A[1:]:
	diff = num - tmp
	max_tmp = max(diff, max_tmp)
	tmp = min(num, tmp)
	max_list.append(diff)

max_val = max(max_list)
c = max_list.count(max_val)
print(c)