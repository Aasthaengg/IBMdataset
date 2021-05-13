n = int(input())
ans = [0 for _ in range(10004)]
for i in range(1,102):
    for j in range(1,102):
        for k in range(1,102):
            v=i*i+j*j+k*k+i*j+j*k+k*i
            if(v<10004):
                ans[v]+=1
for i in range(1,n+1):
    print(ans[i])