N,M,K = map(int,input().split())
flag = 0
if (N*M)%2==0 and K==(N*M)//2:
    flag = 1
else:
    y = 0
    while y<=N:
        if N-2*y!=0 and (K-M*y)%(N-2*y)==0 and M>=(K-M*y)//(N-2*y)>=0:
            flag = 1
            break
        y += 1
if flag==1:
    print("Yes")
else:
    print("No")