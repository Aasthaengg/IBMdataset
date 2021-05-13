import sys
n = int(input())
input_lines = [input() for i in range(n)]
char_set = set()
for i in range(n):
    line = input_lines[i].split()
    if line[0] == 'insert':
        char_set.add(line[1])
    elif line[0] == 'find' and line[1] in char_set:
        print('yes')
    else:
        print('no')
