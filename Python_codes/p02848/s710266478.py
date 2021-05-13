n = int(input())
a = ord('A')
s = [chr((ord(c) - a + n) % 26 + a) for c in input()]
print(''.join(s))