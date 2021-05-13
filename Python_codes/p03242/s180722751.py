n = input()

mapping_table = str.maketrans({'1': '9', '9': '1'})

print(n.translate(mapping_table))
