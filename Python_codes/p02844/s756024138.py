digits = int(input())
num_list = [int(i) for i in list(input())]
flag1 = 0
flag2 = 0
counter = 0


for num1 in range(10):
	for num2 in range(10):
		for num3 in range(10):
			flag1 = 0
			flag2 = 0
			for digit in range(digits):
				if flag1 == 0 and flag2 == 0 and num1 == num_list[digit]:
					flag1 = 1
					continue
				if flag1 == 1 and num2 == num_list[digit]:
					flag2 = 1
					flag1 = 0
					continue
				if flag2 == 1 and num3 == num_list[digit]:
					counter += 1
					flag2 = 0
					break
print(counter)

