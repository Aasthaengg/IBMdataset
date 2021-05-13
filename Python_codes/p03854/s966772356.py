s = list(input())

words = ['dream', 'dreamer', 'erase', 'eraser']
ans = 'YES'

pointer = len(s)
while pointer > 0:
    if s[pointer-5: pointer] == list(words[0]):
        pointer -= 5
    elif s[pointer-5: pointer] == list(words[2]):
        pointer -= 5
    elif s[pointer-7: pointer] == list(words[1]):
        pointer -= 7
    elif s[pointer-6: pointer] == list(words[3]):
        pointer -= 6
    else:
        ans = 'NO'
        break

print(ans)
