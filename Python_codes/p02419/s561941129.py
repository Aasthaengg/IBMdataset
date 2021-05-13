word = input().lower()
count = 0
while 1:
    array = input().split()
    if array[0] == "END_OF_TEXT":
        break

    for a in array:
        if a.lower() == word:
            count += 1

print(count)