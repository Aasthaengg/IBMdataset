N,M = [int(x) for x in input().split()]
li = [0]*N
for _ in range(M):
    a,b = [int(x)-1 for x in input().split()]
    li[a]+=1
    li[b]+=1
for l in li[1:]:
    if(l%2!=0):
        print('NO')
        break
else:
    print('YES')
    
