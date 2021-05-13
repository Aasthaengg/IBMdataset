n,r=int(input()),[]
for i in range(1, n+1):
    for j in range(i+1,n+1):
        if n-i+(n%2==0)!=j:r.append([i, j])
print(len(r))
for i in r:print(*i)