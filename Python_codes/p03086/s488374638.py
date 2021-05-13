N =list(str(input()))
l=['A','C','G','T']

ans=0
for i in range(len(N)):
    num=0
    for u in range(len(N)-i):
        #print(N[i+u])
        if N[i+u] in l:
            num+=1
        else:
            break
    ans=max(ans,num)        
print(ans)