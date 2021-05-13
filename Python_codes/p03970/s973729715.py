s = input()

print(len([a for a, b in zip("CODEFESTIVAL2016", s) if a != b]))
