from collections import Counter
inp=list(map(int,input().split()))
l=inp[0]
r=inp[1]
c=Counter([])
arr=[]
for i in range(l,r+1):
    if c[(i%2019)]==0:
        c[(i%2019)]+=1
        arr.append((i%2019))
        continue
    else:
        break
if c[0]!=0:
    print (0)
else:
    ans=99999999999
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            ans=min(ans,(arr[i]*arr[j])%2019)
            if ans==0:
                break
        if ans==0:
            break
    print (ans)