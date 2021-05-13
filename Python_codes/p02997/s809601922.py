N,K=map(int,input().split())
if K>(N-1)*(N-2)//2:
    print(-1)
else:
    ans=(N-1)*(N-2)//2-K
    print(ans+N-1)
    node=[]
    for i in range(2,N+1):
        node.append((1,i))
    count=0
    for i in range(2,N):
        for j in range(i+1,N+1):
            if count<=ans:
                node.append((i,j))
                count+=1
            else:
                break
    for i in range(ans+N-1):
        print(*node[i])