word_count = 0
W = input().lower()
while True:
    try:
        T = input()
        if T == "END_OF_TEXT":
            break
    except EOFError:
        break
    for Ti in T.lower().split():
        if Ti == W:
            word_count += 1
print(word_count)