N,M,K=map(int,input().split())

for i in range(N+1):
    for j in range(M+1):
        if i==0 or j==0:
            x=N*j+M*i
            if x==K:
                print("Yes")
                exit()
        x=N*j+M*i-(i*j)-i*j
        #print(str(i)+" "+str(j))
        #print(x)
        if x==K:
            print("Yes")
            exit()
print("No")