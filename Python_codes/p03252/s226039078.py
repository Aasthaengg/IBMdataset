S=input()
T=input()
alp=[chr(i) for i in range(97, 97+26)]
words_T=[[] for _ in range(len(alp))]
words_S=[[] for _ in range(len(alp))]
num=0
for al in alp:
    for n in range(len(T)):
        if T[n]==al:
            words_T[num].append(n)
    num+=1
num=0
for al in alp:
    for n in range(len(T)):
        if S[n]==al:
            words_S[num].append(n)
    num+=1
flag=0
for word in words_T:
    if len(word)<=1:
        continue
    wo=S[word[0]]
    for w in word:
        if wo==S[w]:
            continue
        else:
            flag=1
            break
for word in words_S:
    if len(word)<=1:
        continue
    wo=T[word[0]]
    for w in word:
        if wo==T[w]:
            continue
        else:
            flag=1
            break
if flag==0:
    print('Yes')
else:
    print('No')
