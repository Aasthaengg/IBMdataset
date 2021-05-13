s=list(input())
ans=[]
for i in range(1<<(len(s)-1)):
    tmp=0
    num=s[0]
    for j in range(len(s)-1):
        if (i>>j)%2==0:
            num+=s[j+1]
        else:
            tmp+=int(num)
            num=s[j+1]
        #print(num)
    tmp+=int(num)
    ans.append(tmp)
print(sum(ans))