N=int(input())
sets=[]
if N%2==1:
    sets.append([N])
    for i in range(1,N//2+1):
        sets.append([i,(N-i)])
else:
    for i in range(1,N//2+1):
        sets.append([i,N+1-i])
#print(sets)
path=[]
for i in range(len(sets)):
    for j in range(i+1,len(sets)):
        for k in sets[i]:
            for l in sets[j]:
                path.append([min(k,l),max(k,l)])
#print(path)
print(len(path))
for i in path:
    print(*i)
