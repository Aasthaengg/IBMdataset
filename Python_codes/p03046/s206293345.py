import sys
import itertools
m,k=map(int,input().split())
if k>=2**m:
    print(-1)
    sys.exit()

if m==0:
    if k==0:
        print("0 0")
    else:
        print(-1)
    sys.exit()
if m==1:
    if k==0:
        print("1 1 0 0")
    else:
        print(-1)
    sys.exit()
    
lst=[]
for i in range(m):
    if (k>>i)&1==1:
        lst.append(2**i)
    
ans_1=[]
for i in range(2**m):
    if i in lst:
        continue
    else:
        ans_1.append(i)

ans_1+=lst
ans_2=[]
for i in range(2**m-1,-1,-1):
    if i in lst:
        continue
    else:
        ans_2.append(i)
ans_2+=lst[::-1]
ans=ans_1+ans_2
print(*ans)