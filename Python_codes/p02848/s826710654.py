N = int(input())

result = []

for c in input():
    r = ord(c) + N

    # Zを超えている
    if r > 90:
        r = 65 + r % 90 - 1

    result.append(chr(r))

print(''.join(result))
