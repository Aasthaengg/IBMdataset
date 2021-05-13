import sys
input=sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))
for i in range(n):
    lst[i]=[lst[i]]
for i in range(n):
    lst[i].append(i)
lst=sorted(lst,key=lambda x:x[0])
ans=[]
for i in lst:
    ans.append(i[1]+1)
print(" ".join(map(str,ans)))