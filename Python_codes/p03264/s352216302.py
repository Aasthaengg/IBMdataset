k = int(input())

if k % 2 == 1:
	odd_num = (k + 1)/2
	even_num = (k - 1)/2
else:
	odd_num = k/2
	even_num = k/2
	
print(int(odd_num * even_num))