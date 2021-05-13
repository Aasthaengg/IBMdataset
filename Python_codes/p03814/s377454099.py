s = input()

answer = 0
a = 0
z = 0

words = list(s)

for num in range(len(words)):
    if words[num] == 'A':
        a = num
        break

for num in range(len(words)):
    if words[num] == 'Z':
        z = num

answer = z - a + 1

print(answer)


