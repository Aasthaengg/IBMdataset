S = input()
prev = S[0]
count = 0
for c in S:
    if prev != c:
        count += 1
        prev = c
print(count)