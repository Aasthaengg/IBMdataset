S = input()
point = 0

if len(S)%2 == 0:
    for i in range(0,len(S),2):
        if S[i] in 'RUD' and S[i+1] in 'LUD':
            point += 2

if len(S)%2 == 1:
    if S[0] in 'RUD':
        point += 1
    for i in range(1,len(S),2):
        if S[i+1] in 'RUD' and S[i] in 'LUD':
            point += 2

if point == len(S):
    print('Yes')
else:
    print('No')
