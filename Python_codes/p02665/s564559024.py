n=int(input())
l=list(map(int,input().split()))
k=l[n]
count=1
sumleaf=1
flag=True
i0=0
suml=[]
for i in l:
    i0+=i
    suml.append(i0)
if l[0]>2 or l[0]==1 and n>=1:
    print(-1)
    flag=False
elif n==0 and l[0]!=1:
    print(-1)
    flag=False
    
else:
    for i in range(1,n+1):
        sumleaf*=2
        if i==n and sumleaf<k:
            flag=False
            print(-1)
            break
        elif i==n:
            count+=k
        else:
            if sumleaf<=l[i]:
                flag=False
                print(-1)
                break
            else:
                sumlnew=suml[n]-suml[i-1]
                count+=min(sumlnew,sumleaf)
                sumleaf=min(sumlnew,sumleaf)-l[i]
    
                    
                    
                    
                    
                
if flag==True:
    print(count)