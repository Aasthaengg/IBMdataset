k,s = list(map(int, input().split()))
cnt=0
minX=max(s-2*k, 0)
maxX=min(s, k)
for x in range(minX, maxX+1):
    rest=s-x
    if k>=rest:
        cnt+=rest+1
    else:
        cnt+=2*k-rest+1
    
print(cnt)