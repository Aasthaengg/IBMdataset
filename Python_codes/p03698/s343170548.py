S = input()

for i in range(len(S)):
    if S.count(S[i]) > 1:
        print('no')
        exit()
print('yes')
