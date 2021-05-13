R,G,B,N = list(map(int,input().split()))
cnt = 0
for i in range(N+1):
    for j in range(N+1):
        k = (N-R*i-G*j)//B
        if i>=0 and j>=0 and k>=0 and R*i+G*j+B*k==N:
            cnt+=1
print(cnt)