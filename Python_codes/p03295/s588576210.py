n,m=map(int,input().split(' '))
war=[tuple(map(int,input().split(' '))) for _ in range(m)]
war.sort(key=lambda x:x[1])
bridge=[0]*n
flag=0
for w in war:
    if not w[0]<=flag<w[1]:
        flag=w[1]-1
        bridge[flag]=1
print(sum(bridge))