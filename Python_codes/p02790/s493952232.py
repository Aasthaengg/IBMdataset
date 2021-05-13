a,b = map(int,input().split())

words = []
a_word = ""
b_word = ""

for i in range(a):
    b_word += str(b)
for i in range(b):
    a_word += str(a)
words.append(a_word)
words.append(b_word)
words.sort()

print(words[0])