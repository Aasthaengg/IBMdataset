N = int(input())
S = str(input())

tmp=0
tmp_max=0
for i in range(N):
    if S[i]=='I':
        tmp+=1
        if tmp>=tmp_max:
            tmp_max=tmp
    else:
        tmp-=1
print(tmp_max)