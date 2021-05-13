numbers = input()
i = 0
while i <= 2:
    if numbers[i] == numbers[i + 1]:
        print("Bad")
        exit()
    else:
        i += 1

print("Good")