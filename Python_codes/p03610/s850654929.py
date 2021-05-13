s = input()

count = 0
result = ""

for x in s:
    count = count +1
    if count % 2 == 1:
        result = result + x
else:
    print(result)