b = input()

print(b.translate(str.maketrans({'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'})))
