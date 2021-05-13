arr=list(map(str,input()))
R=[]
L=[]
count=0
ans=[0]*len(arr)

kari="R"
for i in range(len(arr)):
    if arr[i]==kari:
      count+=1
    else:
        if kari=="R":
            R.append(count)
        else:
            L.append(count)
        kari=arr[i]
        count=1
L.append(count)

aa=0
for i in range(len(R)):
    a=R[i]+L[i]
    aa+=a
    if a%2==0:
        ans[aa-L[i]]=a//2
        ans[aa-L[i]-1]=a//2
    elif a%2==1 and L[i]%2==0:
        ans[aa-L[i]]=a//2
        ans[aa-L[i]-1]=a//2+1
    else:    
        ans[aa-L[i]]=a//2+1
        ans[aa-L[i]-1]=a//2
        
print(*ans)