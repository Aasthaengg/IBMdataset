b = input()

# if b == 'A':
#     print('T')
# elif b == 'T':
#     print('A')
# elif b == 'C':
#     print('G')
# elif b == 'G':
#     print('C')
# else:
#     pass

pattern = {
    'A':'T',
    'T':'A',
    'C':'G',
    'G':'C'
}

print(pattern[b])