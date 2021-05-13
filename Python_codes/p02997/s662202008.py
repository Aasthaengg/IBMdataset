

def resolve():
    N,K =map(int,input().split())

    if K > ((N-1)*(N-2))//2:
        print(-1)
        return
    XX = [(1,i) for i in range(2,N+1)]
    xx2=[]
    for i in range(2,N+1):
        for j in range(i+1,N+1):
            xx2.append((i,j))

    xx2 = xx2[:((N-1)*(N-2))//2-K]

    ans = XX+xx2
    print(len(ans))

    for i,j in ans:
        print(i,j)    



if __name__ == "__main__":
    resolve()