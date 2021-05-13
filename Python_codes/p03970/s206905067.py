correct = "CODEFESTIVAL2016"
s = input()
count = 0
for k,i in zip(correct,s):
	if k != i:
		count+= 1
print(count)