S1=list(input())
S2=list('CODEFESTIVAL2016')
cnt=0
for i in range(len(S1)):
    if S1[i]!=S2[i]:
        cnt=cnt+1

print(cnt)
