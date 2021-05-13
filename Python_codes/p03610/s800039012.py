S = input()
List = []
for i in range(len(S)):
    if i % 2 == 0:
        List.append(S[i])
print(''.join(List))