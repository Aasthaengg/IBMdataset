s = input() + " "
print("".join([s[q] for q in range(len(s)) if q % 2 == 0]).rsplit()[0])