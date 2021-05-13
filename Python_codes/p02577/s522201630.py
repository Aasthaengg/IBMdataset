x = input()
if sum([int(i) for i in x]) % 9 == 0:
    print("Yes")
else:
    print("No")