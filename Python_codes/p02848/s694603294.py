n = int(input())
print(''.join(map(lambda x: chr((ord(x) + n + 13) % 26 + 65), input())))