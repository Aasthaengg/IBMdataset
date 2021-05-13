member = []
count = 0
name_count = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
N = int(input())
for i in range(N):
    name = input()
    member.append(name)
for i in range(N):
    if member[i][0] in name_count:
        name_count[member[i][0]] += 1
count += name_count['M'] * name_count['A'] * name_count['R']
count += name_count['M'] * name_count['A'] * name_count['C']
count += name_count['M'] * name_count['A'] * name_count['H']
count += name_count['M'] * name_count['R'] * name_count['C']
count += name_count['M'] * name_count['R'] * name_count['H']
count += name_count['M'] * name_count['C'] * name_count['H']
count += name_count['A'] * name_count['C'] * name_count['R']
count += name_count['A'] * name_count['H'] * name_count['R']
count += name_count['A'] * name_count['H'] * name_count['C']
count += name_count['H'] * name_count['C'] * name_count['R']
print(count)
