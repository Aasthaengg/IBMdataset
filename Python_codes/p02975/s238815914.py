import sys
n=int(input())
a=sorted(list(map(int,input().split())))

p=set(a[:n//3])
q=set(a[n//3:(n//3)*2])
r=set(a[(n//3)*2:n])

flag=True
if n%3!=0:
    flag=False
if len(set(a))==1 and a[0]==0:
    print("Yes")
    sys.exit()
    
if flag and len(p)==1 and len(q)==1 and len(r)==1:
    if a[0] ^ a[n//3]==a[(2*n)//3]:
        print("Yes")
    else:
        print("No")
else:
    print("No") 
