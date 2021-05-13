s = input()
length = 0
max_length = 0

for i in range(len(s)):
    if s[i] in 'ACGT':
        length += 1
    else:
        length = 0
    if length > max_length:
        max_length = length
print(max_length)  