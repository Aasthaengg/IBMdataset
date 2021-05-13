S = input()
T = input()
count = 0
for i,char in enumerate(S):
    if char != T[i]:
        count += 1

print(count)
