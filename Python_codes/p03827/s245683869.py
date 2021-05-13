p = input()
s = input()

words = list(s)
x = 0
max_x = 0
n = int(p)

for num in range(len(words)):
    if words[num] == 'I':
        x += 1
        if x > max_x:
            max_x = x
    else:
        x -= 1

print(max_x)

