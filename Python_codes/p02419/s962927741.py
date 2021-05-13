count = 0
s = ""
array =[]
while True:
    count += 1
    if count == 1:
        s = input()
    n = input()
    if n == "END_OF_TEXT":
        break
    array.append(n)
count = 0
for i in range(len(array)):
    for i2 in array[i].split():
        if s.upper() == i2.upper() or s.lower() == i2.lower():
            count += 1
print(count)