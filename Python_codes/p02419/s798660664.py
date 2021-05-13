word = input().lower()
count = 0
while True:
    line = input()
    if line == "END_OF_TEXT":
        break
    words = line.lower().split()
    for w in words:
        if w == word:
            count += 1
print(count)