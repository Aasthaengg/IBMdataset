N = int(input())
H = list(map(int,input().split()))
ans,buf=0,0
for i in range(0,len(H)-1):
    if H[i] >= H[i+1]:
        buf += 1
    else:
        ans = max(ans,buf)
        buf = 0
ans = max(ans,buf)
print(ans)        
