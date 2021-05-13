b = input()

base_pairs = {
    'A': 'T', 
    'C': 'G',
    'G': 'C',
    'T': 'A',
}

pair = base_pairs.get(b)

print(pair)
