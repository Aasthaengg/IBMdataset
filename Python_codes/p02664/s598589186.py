T = input()
line = [c for c in T]

for i in range(len(line)):
    if line[i] == '?':
        line[i] = 'D'

print("".join(line))