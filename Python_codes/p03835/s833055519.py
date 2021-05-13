K,S=map(int,input().split())

ans=0
for z in range(K+1):
    tmp=S-z
    for x in range(K+1):
        if x+K<tmp:
            continue
        if x>tmp:
            break
        ans+=1
print(ans)