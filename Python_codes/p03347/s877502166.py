# coding: utf-8
# Your code here!
N=int(input())

pre=int(input())
if pre!=0:
    print(-1)
    exit()

ans=0
count=0
for _ in range(N-1):
    A=int(input())
    if A-pre>1:
        print(-1)
        exit()
    if A==pre:
        count+=1
    else:
        ans+=pre*count
        if A<pre:
            ans+=(A-1)
        ans+=1
        count=0
        #print(_,ans)
    pre=A

print(ans+pre*count)