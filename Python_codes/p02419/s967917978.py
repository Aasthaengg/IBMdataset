word = raw_input()
counter = 0
while True:
    line = raw_input()
    if line == "END_OF_TEXT":
        break
    counter += line.lower().split(" ").count(word)

print counter