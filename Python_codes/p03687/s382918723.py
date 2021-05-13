import string
d = {}
alph = string.ascii_lowercase
for i in range(len(alph)):
    d[alph[i]] = i
s = list(input())


count = [0 for _ in range(len(alph))]
for letter in s:
    count[d[letter]] += 1
# print(count)

target = []
for i in range(len(alph)):
    if count[i] == max(count):
        target.append(alph[i])

# print(target)
answer = []
for t in s:
    time = 0
    size = len(s)
    line = list(s)
    ifOK = True
    while ifOK:
        # print("".join(line))
        ifOK = False
        new_line = ""
        for i in range(size-1):
            if (line[i] == t or t == line[i+1]) and not line[i] == line[i+1]:
                new_line += t
                ifOK = True
            else:
                new_line += line[i]
        line = list(new_line)
        size -= 1
        time += 1
    answer.append(time)
print(min(answer)-1)
