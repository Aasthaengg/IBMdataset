from collections import  deque
n=int(input())
a=list(map(int,input().split()))
cnt=0
judge=[]
for i in range(n-1):
    if a[i]<a[i+1]:
        flag=0
    elif a[i]>a[i+1]:
        flag=1
    elif a[i]==a[i+1]:
        continue
    if judge==[]:
        judge.append(flag)
    else:
        ff=judge.pop()
        if flag==ff:
            judge.append(flag)
        else:
            cnt+=1

print(cnt+1)