import sys
n=int(input())
a=list(map(int,input().split()))
if n==1:
    print(1)
    sys.exit()
k=1
s=a[0]
lst=[0]*n
for i in range(n):
    while s^a[k]==s+a[k]:
        s+=a[k]
        k+=1
        if k==n:
            for j in range(i,n):
                lst[j]=n-j
            break
    else:
        lst[i]=k-i
        s=s^a[i]
        continue
    break
print(sum(lst))