n,h,w=map(int,input().split())
ab=[]
for i in range(n):
    ab.append(list(map(int,input().split())))
#print(ab)

ans=0

for i in range(n):
    if(ab[i][0]>=h and ab[i][1]>=w):
        ans+=1
print(ans)