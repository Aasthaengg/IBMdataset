word_s = input()
word_t = input()

if(len(word_s) <= 10 and len(word_s) >= 1 and len(word_t) == len(word_s) + 1 and word_s == word_t[:-1]):
    print("Yes")
else:
    print("No")