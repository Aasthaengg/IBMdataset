target = input()

count = 0
while True:
    line = input()
    if line == 'END_OF_TEXT':
        break

    for word in line.split():
        if word.lower() == target.lower():
            count += 1

print(count)