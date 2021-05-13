X=input()
t=0
s=0
ans=0
for i in range(len(X)):
    if X[i]=="T":
        t+=1
    else:
        s+=1
    ans=max(ans,t-s)
print(ans*2)