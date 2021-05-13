s = input()
l = list(s)

numl = []
for i in range(len(l) - 2):
    num = int(l[i] + l[i + 1] + l[i + 2])
    numl.append(num)

diffl = []
for i in numl:
    diff = abs(753 - i)
    diffl.append(diff)

print(min(diffl))