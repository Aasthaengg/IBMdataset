S = input()
T = input()

count = 0

for i,s in enumerate(S):
    if T[i] == s:
        count += 1
print(count)
