S = input()
T = ''

add_word = ['eraser', 'erase', 'dreamer', 'dream']

for word in add_word:
    S = S.replace(word, '')

if S == T:
    ans = 'YES'
else:
    ans = 'NO'

print(ans)