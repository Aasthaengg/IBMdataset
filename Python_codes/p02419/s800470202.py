word = raw_input()
count = 0

while 1:
    line = raw_input()
    if line == "END_OF_TEXT":
        break
    for target in line.split(" "):
        if word.lower() == target.lower():
            count += 1

print(count)