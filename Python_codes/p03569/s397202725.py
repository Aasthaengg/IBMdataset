S = input()

S_rmv =S.replace('x','')

count = 0
if S_rmv == S_rmv[::-1]:
    i = 0
    j = len(S)-1
    while i<j:
        if S[i] == S[j]:
            i +=1
            j -=1
        elif S[i] == 'x':
            i +=1
            count +=1
        elif S[j] == 'x':
            j -=1
            count +=1
    print(count)
else:
    print(-1)