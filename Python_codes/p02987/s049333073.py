S = list(input())
S.sort()
if S[0] == S[1] and not S[1]==S[2] and S[2]==S[3]:
    print('Yes')
    exit()
print('No')

