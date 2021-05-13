word = input()
ans = []
j = 0
for i in word:
    j += 1

if word[j - 1] != 's':
    ans = word + 's'
elif word[j - 1] == 's' and j >= 1:
    ans = word + 'es'
print(ans)