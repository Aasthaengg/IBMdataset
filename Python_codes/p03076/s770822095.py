import math
abcde = [input() for i in range(5)]

flg = -1
for i in range(1,10):
    if flg != -1:
        break
    for j in range(5):
        if abcde[j][-1]==str(i):
            flg = j
            break
total = 0
for i in range(5):
    if flg==i:
        total += int(abcde[i])
    else:
        total += math.ceil(int(abcde[i])/10)*10
print(total)