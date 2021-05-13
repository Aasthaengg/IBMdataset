X=input()

ans=0
for i in range(len(X)):
    if X[i]=='S':
        ans+=1
    else:
        if ans==0:
            ans=0
        else:
            ans-=1
print(ans*2)