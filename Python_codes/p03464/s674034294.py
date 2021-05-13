k = int(input())
ai = [int(i) for i in input().split()]

low = 2
high = 2*10**15
ans = []

while low+1 < high:
    tmp = 0
    mid = (low + high) //2
    #print(mid)
    tmp = mid
    
    for i in range(k):
        tmp = tmp // ai[i]
        tmp = tmp*ai[i]
    #print(tmp,mid,low)
    
    if tmp > 2:
        high = mid
    else:
        low = mid

tmp = low

for i in range(k):
    tmp = tmp // ai[i]
    tmp = tmp*ai[i]

if tmp != 2:
    print(-1)
    exit()
        
ans.append(low)

low = 2
high = 2*10**15

flag = True

while low+1 < high:
    tmp = 0
    mid = (low + high) //2
    if flag == True:
        flag = False
        mid = 2
    #print(mid)
    tmp = mid
    
    for i in range(k):
        tmp = tmp // ai[i]
        tmp = tmp*ai[i]
    #print(tmp)
    
    if tmp > 1:
        high = mid
    else:
        low = mid
    #print(mid)
ans.append(high)
tmp = high
for i in range(k):
    tmp = tmp // ai[i]
    tmp = tmp*ai[i]

if tmp != 2:
    print(-1)
    exit()
print(ans[1],ans[0])