a,b,c=[int(x) for x in input().split()]
cnt=0
for d in range(a,b+1): 
    if c%d==0: cnt+=1
print(cnt)