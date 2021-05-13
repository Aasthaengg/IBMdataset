S=input()
T=input()

ans='Yes'
for s_idx,s in enumerate(S):
    if s != T[s_idx]:
        ans='No'
        
print(ans)