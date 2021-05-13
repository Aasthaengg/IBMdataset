S=input()
T='CODEFESTIVAL2016'
cnt=0

for i, w in enumerate(T):
    if w != S[i]:
        cnt+=1
print(cnt)