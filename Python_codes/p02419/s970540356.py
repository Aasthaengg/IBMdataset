key = input()

cnt = 0
while True:
    line = input()
    if line == 'END_OF_TEXT':
        break

    cnt += sum([key == word for word in line.lower().split()])

print(cnt)