n,m = [int(i) for i in input().split()]
p = ['P']*n
k = ['I']*m
al = p+k
ans = 0
for i in range(len(al)):
    for j in range(i+1,len(al)):
        if al[i] == 'I' and al[j]=='I':ans+=1
        if al[i] == 'P' and al[j] == 'P': ans+=1
print(ans)