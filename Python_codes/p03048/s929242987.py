rgb = [0]*3
rgb[0],rgb[1],rgb[2],n = map(int,input().split())
rgb.sort()

ans=0
for i in range(n//rgb[2]+1):
    for j in range((n-i*rgb[2])//rgb[1]+1):
        d = n-i*rgb[2]-j*rgb[1]
        if d%rgb[0]==0 and d>=0:
            ans+=1

print(ans)