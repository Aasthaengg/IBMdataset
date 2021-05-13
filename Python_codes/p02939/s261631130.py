ans=0
S=T=''
for i in input():
    S+=i
    if S!=T:
        ans+=1
        S,T='',S
print(ans)