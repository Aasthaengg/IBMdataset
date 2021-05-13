S = input()
T = input()
i = 0
count = 0
for s in S:
    if s != T[i]:
        count = count + 1
    i = i + 1
print(count)