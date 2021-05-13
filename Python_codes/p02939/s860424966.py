S=input()
ans=0
l=["hoge"]
j=0
for i in range(len(S)):
    if S[j:i+1]==l[-1]:
        continue
    else:
        l.append(S[j:i+1])
        ans+=1
        j=i+1
    #print(l)
print(ans)