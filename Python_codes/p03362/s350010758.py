n = int(input())
prime = [2]
A = 55555
for L in range(3, A, 2):
    for L2 in prime:
        if L % L2 == 0:
            break
    else:
        prime.append(L)

cnt=0
ans=[]
for p in prime:
    if p%5==1:
        ans.append(p)
        cnt+=1
    if cnt==n:
        break
print(*ans)