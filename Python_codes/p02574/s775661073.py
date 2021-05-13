n=int(input())
a=list(map(int,input().split()))
temp=[0]*(10**6+1)
for i in a:
    temp[i]+=1
if temp[1]==n:
    print("pairwise coprime")
    exit()
ans=[]
for i in range(2,10**6+1):
    count=0
    j=1
    while True:
        count+=temp[i*j]
        j+=1
        if i*j>=10**6:
            break
    ans.append(count)
if max(ans)==1:
    print("pairwise coprime")
elif max(ans)==n:
    print("not coprime")
else:
    print("setwise coprime")
