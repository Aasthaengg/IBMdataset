def get_char_set(word):
    char_index = {}
    for i, c in enumerate(word):
        if c not in char_index.keys():
            char_index[c] = []
        char_index[c].append(i)
    char_set = set()
    for char_index_list in char_index.values():
        char_set.add(tuple(char_index_list))
    return char_set

s = input()
t = input()

s_char_set = get_char_set(s)
t_char_set = get_char_set(t)
if s_char_set == t_char_set:
    print('Yes')
else:
    print('No')
