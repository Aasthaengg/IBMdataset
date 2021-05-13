t = []
w = input()
while True:
    line = input()
    if line == "END_OF_TEXT":
        break
    for word in line.lower().split():
        t.append(word)
print(t.count(w))