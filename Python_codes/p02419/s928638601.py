key_word = input().lower()
counter = 0
while True:
    sentences = input().split()
    if sentences == ['END_OF_TEXT']:
        break
    for sent in sentences:
        if sent.lower() == key_word:
            counter += 1
print(counter)

