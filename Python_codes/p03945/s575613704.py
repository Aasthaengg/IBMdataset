s = input()
print(sum(a != b for a, b in zip(s, s[1:])))
