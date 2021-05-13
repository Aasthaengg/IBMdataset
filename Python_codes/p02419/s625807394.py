w = input()
count = 0
while True:
    text = input()
    if text == "END_OF_TEXT":
        break
    words = [w.lower() for w in text.split()]
    for word in words:
        if w == word:
            count += 1
print(count)
    
