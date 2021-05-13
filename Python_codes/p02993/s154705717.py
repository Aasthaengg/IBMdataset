numbers = input()
i = 0
x = 1
while i <= 2:
    if numbers[i] == numbers[x]:
        print("Bad")
        exit()
    else:
        i += 1
        x += 1

print("Good")