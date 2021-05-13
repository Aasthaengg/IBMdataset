S = input()
ans = []
count = 0
for i in range(len(S)):
    if int(S[i]) == 2:
        count += 1
print(count)