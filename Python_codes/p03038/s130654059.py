n,m,*abc=map(int,open(0).read().split())
a=abc[:n]
a.sort()
bc=[[x,y] for x,y in zip(abc[n::2],abc[n+1::2])]
bc.sort(key=lambda x:x[1],reverse=True)
ai = 0
for b,c in bc:
    cc = b
    while ai<n and cc >0:
        if a[ai] < c:
            a[ai] = c
            cc -= 1
        ai +=1
    if ai ==n:
        break
print(sum(a))
        
