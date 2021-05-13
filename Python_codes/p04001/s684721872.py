S=input()
res=[]
for i in range(2**(len(S)-1),2**(len(S))):
    tmp=''
    for j in range(len(S)):
        if j==len(S)-1:
            tmp+=S[j]
        elif (str(bin(i))[3:])[j]=='1':
            tmp+=S[j]
        else:
            tmp+=S[j]+'+'
    if tmp[-1]=='+':
        tmp=tmp[:-1]
    res.append(eval(tmp))
print(sum(res))