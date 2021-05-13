S=input()
T=input()

ans='Yes'
for x,y in zip(S,T):
    if x!=y:
        ans='No'
        break

print(ans)
