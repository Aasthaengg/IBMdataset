S = input()
N = len(S)

maxLength = 0

count = 0
for i in range(N):
    c = S[i]
    if c == 'A' or c == 'C' or c == 'G' or c == 'T':
        count += 1
    else:
        if maxLength < count:
            maxLength = count
        count = 0

if maxLength < count:
    maxLength = count

print(maxLength)