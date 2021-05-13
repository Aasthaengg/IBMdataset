n = int(input())
a = 0
b = 0
for i in range(n):
    word = list(input().split())
    new_word = sorted(word)
    if word[0] == word[1]:
        a += 1
        b += 1
    elif new_word == word:
        b += 3
    else:
        a += 3
print('{} {}'.format(a, b))
