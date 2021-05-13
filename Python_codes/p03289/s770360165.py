s = input()
start_with_a = s[0] == 'A'
contains_c = s[2:-1].count('C') == 1
all_lowercases = s.replace('A', '').replace('C', '').islower()

print('AC' if all([start_with_a, contains_c, all_lowercases]) else 'WA')