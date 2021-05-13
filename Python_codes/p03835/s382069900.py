K,S=map(int,input().split())
count=0
for i in range(K+1):
    for j in range(K+1):
        if((S-i-j)<=K and 0<=S-i-j):
            count=count+1
print(count)
