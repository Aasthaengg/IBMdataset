n=int(input())
l=[int(i) for i in input().split()]
seen=[0]* 22 
ans=0 
c=0 
st=0 
ans=0 
for end in range(n): 
   # print(seen,end)
    for j in range(22):
        if l[end]&(1<<j):
            if seen[j]==1: 
                while seen[j]:
                    for bit in range(22):
                        if (1<<bit)&l[st]:
                            seen[bit]=0 
                    st+=1 
            else:
                seen[j]=1 
    for j in range(22):
        if l[end]&(1<<j):
            seen[j]=1 
    #print(end,st)
    c=(end-st+1)
   # print(c)
    ans+=c
print(ans)

'''
6
2 4 2  4 3 2
'''