moji = str(input())
dictionary = {}
for i in moji:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1
if len(dictionary) == 2 & dictionary[i] == 2:
    print("Yes")
else:
    print("No")