n=int(input())
s=input()
ans,a=0,[]
for i in range(n):
    if s[i] not in a:
        a+=[s[i]]
        b=[]
        for j in range(i+1,n):
            if s[j] not in b:
                b+=[s[j]]
                c=[]
                for k in range(j+1,n):
                    if s[k] not in c:
                        c+=[s[k]]
                        ans+=1
print(ans)