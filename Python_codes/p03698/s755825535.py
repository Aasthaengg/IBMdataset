s = input()

words = list(s)

check = True

for j in range(len(words)):
    for i in range(len(words) - (j + 1)):
        if words[j] == words[j + i + 1]:
            check = False
            
            break

if check:
    print('yes')
else:
    print('no')