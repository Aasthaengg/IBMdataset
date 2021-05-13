s = input()

A_first_index = s.index('A')
Z_last_index = max([i for i, c in enumerate(s) if c == 'Z'])

print(len(s[A_first_index:Z_last_index+1]))