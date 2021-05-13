import random

s = input()
r = random.randint(0,len(s)-3)

print(s[r:(r+3)])