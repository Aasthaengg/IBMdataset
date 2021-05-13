s = input()
t = input()
print(sum([
    1 if s[0] == t[0] else 0,
    1 if s[1] == t[1] else 0,
    1 if s[2] == t[2] else 0
]))