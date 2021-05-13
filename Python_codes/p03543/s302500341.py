s = input()
counter = 0
for i in range(10):
    if str(i)*3 in s:
        counter += 1
print("Yes") if counter else print("No")