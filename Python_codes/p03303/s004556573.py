import math

s = input()
w = int(input())

num_words = math.ceil(len(s)/w)
letters = []
for i in range(num_words):
    letter = s[i*w]
    letters.append(letter)

ans = ''.join(letters)
print(ans)