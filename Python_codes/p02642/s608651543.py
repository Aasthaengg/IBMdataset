N = int(input())
lineup = sorted([int(x) for x in input().split()])
duplicate={}
for i in lineup:
    if i in duplicate:
        duplicate[i]+=1
    else:
        duplicate[i]=1
b=max(lineup)+1
sieve=[1]*(b)
counter=0
for i in range(N):
    if sieve[lineup[i]]:
        if duplicate[lineup[i]]==1:
            counter+=1
        for j in range(lineup[i],b,lineup[i]):
            sieve[j]=0
        
print(counter)