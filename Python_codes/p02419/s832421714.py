w = input().casefold()
word_count = 0
while True:
    line = input()
    if line == "END_OF_TEXT":
        break
    line = line.casefold()
    word = line.split()
    word_count += word.count(w)
print(word_count)