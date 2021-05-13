S = input() + 'R'

numbers = [0] * (len(S) - 1)

offset = 0
length = 0
right = 0
left = 0
for index, (s0, s1) in enumerate(zip(S, S[1:])):
    length += 1
    if s0 == 'R' and s1 == 'L':
        right = length - 1
        left = length
    elif s0 == 'L' and s1 == 'R':
        if length % 2 == 0:
            numbers[offset + right] = length // 2
            numbers[offset + left] = length // 2
        elif right % 2 == 0:
            numbers[offset + right] = length // 2 + 1
            numbers[offset + left] = length // 2
        else:
            numbers[offset + right] = length // 2
            numbers[offset + left] = length // 2 + 1
        length = 0
        offset = index + 1

print(*numbers)
