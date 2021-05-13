a, b = map(int, input().split())
hw = [["." for i in range(100)] for j in range(50)]
wo = [["#" for i in range(100)] for j in range(50)]
hw += wo
k = 0
for i in range(b-1):
	i = i*2 + 1
	if i%100 == 1 and i//100 > 0:
		k += 2
	hw[k][i%100] = "#"
l = 51
for i in range(a-1):
	i = i*2 + 1
	if i%100 == 1 and i//100 > 0:
		l += 2
	hw[l][i%100] = "."
print (100,100)
for i in range(100):
	print ("".join(hw[i]))