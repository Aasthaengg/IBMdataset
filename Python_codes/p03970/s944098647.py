S=input()
T='CODEFESTIVAL2016'
ans=0
for s,t in zip(S,T):
    if s!=t: ans+=1
print(ans)