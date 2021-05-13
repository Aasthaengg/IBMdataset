S=input()
T=input()
ans='No'
for i in range(100):
    if S==T:
        ans='Yes'
    else:
        tmp=S[-1]
        S=tmp+S[:-1]
print(ans)