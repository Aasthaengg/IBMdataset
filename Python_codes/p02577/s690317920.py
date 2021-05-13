a = list(map(int, list(input())))
sum = sum(a)
if sum % 9 == 0:
    print("Yes")
else:
    print("No")