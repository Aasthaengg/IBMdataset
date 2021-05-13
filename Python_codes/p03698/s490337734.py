S=str(input())
ss=[S[0]]

for i in range(1,len(S)):
    if S[i] in ss:
        print('no')
        break
    else:
        ss.append(S[i])

if len(S)==len(ss):
    print('yes')