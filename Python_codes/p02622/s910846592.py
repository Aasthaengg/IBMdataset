S = input()
T = input()

counter = 0
for i in range(len(S)):
    if S[-i] == T[-i]:
        continue
    else:
        counter += 1

print(counter)