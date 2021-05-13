S = input()

words = ["dream", "dreamer", "erase", "eraser"]
S_rv = S[::-1]
words_rv = [word[::-1] for word in words]

for i in range(len(S_rv)):
    for word_rv in words_rv:
        if S_rv[: len(word_rv)] == word_rv:
            S_rv = S_rv[len(word_rv) :]

if len(S_rv) == 0:
    print("YES")
else:
    print("NO")
