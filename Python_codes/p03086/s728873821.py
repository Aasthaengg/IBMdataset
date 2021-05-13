S = input()
count = 0
max = 0
for i in range(len(S)):
    if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
        count += 1
    else:
        if max < count:
            max = count
        count = 0
if max < count:
    max = count
print(max)
