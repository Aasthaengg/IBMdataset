s = input()
print(min(max(map(len, s.split(a))) for a in s))