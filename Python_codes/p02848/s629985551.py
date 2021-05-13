n = int(input())
s = input()
print(*[chr(65 + (ord(si) - 65 + n) % 26) for si in s], sep='')