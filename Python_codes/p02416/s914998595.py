while True:
    letters = input()
    if letters == '0':
        break
    sumed = 0
    for letter in letters:
        sumed += int(letter)
    print(sumed)
   