n=int(input())
blist=list(map(int,input().split()))
alist=[blist[-1]]

for i in range(n-1):
    tmp = blist[-(i+1)]
    alist[i] = min(alist[i],tmp)
    alist.append(tmp)

print(sum(alist))

