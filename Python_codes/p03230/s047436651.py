import sys


n=int(input())

if n==1:
    print('Yes')
    print(2)
    print(1,1)
    print(1,1)
    sys.exit()

k=3
while True:
    if (k-1)*k//2<n:
        k+=1
    elif (k-1)*k//2==n:
        break
    else:
        print('No')
        sys.exit()

print('Yes')
print(k)

def divide(x,y):#x=n,y=k
    if x==3:
        return [[1,2],[2,3],[3,1]]
    else:
        res=divide(x-(y-1),y-1)
        for i in range(y-1):
            res[i].append((x-y+2)+i)
        res.append([i for i in range(x-y+2,x+1)])
        return res


Ans=divide(n,k)
for ans in Ans:
    print(k-1,*ans)









