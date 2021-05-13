R, G, B, n=map(int, input().split())

r=n//R
g=n//G
b=n//B

cnt=0
for i in range(r+1):
    for j in range(g+1):
        tmp = i*R + j*G
        if (n-tmp)%B == 0 and 0 <= (n-tmp)//B :
            cnt+=1


print(cnt)