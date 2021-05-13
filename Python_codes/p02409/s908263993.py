def print_list(lst) :
	a = ' '.join(list(map(str, lst)))
	print(" " + a)

n = int(input())
lst = [[[0 for w in range(10)] for q in range(3)] for e in range(4)]
for _ in range(n):
	b,f,r,v = list(map(int, input().split()))
	lst[b-1][f-1][r-1] += v 
for i in range(4):
	if (i != 0):
		print("#" * 20)
	for j in range(3):
		print_list(lst[i][j])