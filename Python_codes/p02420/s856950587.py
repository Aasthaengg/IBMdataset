while True:
    word = raw_input()
    if "-" == word:
        break
 
    n = int(raw_input())

    for i in range(n):
        h = int(raw_input())
        word = word[h:] + word[:h]
    print word