numbers = input().split(" ")
sol_count = 0
for walkaz in range(int(numbers[0]), int(numbers[1])+1):
	if(int(numbers[2])%walkaz == 0):
		sol_count += 1

print(sol_count)