N,K=map(int, input().split())


if K>((N-1)*(N-2)//2):
    print(-1)
    exit()

#最大値　(N-1)(N-2)//2
G=[]
for i in range(2,N+1):
    G.append((1,i))

res=(N-1)*(N-2)//2-K

count=0
flag=False
for i in range(2,N):
    for j in range(i+1,N+1):
        if count<res:
            G.append((i,j))
            count+=1
        if count==res:
            flag=True
            break
    if flag:
        break

print(len(G))
for t in G:
    a,b=t
    print(a,b)
