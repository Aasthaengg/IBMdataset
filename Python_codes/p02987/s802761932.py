S = input()
result = 'Yes'
for i in range(len(S)):
    if S.count(S[i]) != 2:
        result = 'No'
print(result)