S = input()
is_easy = True

for i in range(len(S)):
    if i & 1 == 1 and S[i] == 'R':
        is_easy = False
        break
    if i & 1 == 0 and S[i] == 'L':
        is_easy = False
        break

print(['No', 'Yes'][is_easy])