N = int(input())
H = list(map(int,input().split()))
count = 0
ans = 0
posi = H[0]
for i in range(1,N):
    if(posi>=H[i]):
        posi = H[i]
        count +=1
    else:
        posi = H[i]
        ans=max(ans,count)
        count=0
print(max(ans,count))