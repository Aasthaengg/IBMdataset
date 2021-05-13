S = [x for x in input()]
flg=False
for i in range(len(S)-1):
    for j in range(i+1, len(S)):
        if S[i]=='C' and S[j]=='F':
            flg=True
            break
ans='Yes' if flg else 'No'
print(ans)