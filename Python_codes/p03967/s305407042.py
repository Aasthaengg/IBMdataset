s = input()

s = [c == 'g' for c in s]

print(sum(s[1::2]) - sum(not f for f in s[::2]))