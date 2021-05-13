import sys
input=sys.stdin.readline
n,q=map(int,input().split())
s=input().rstrip()

lst=[0]
for i in range(1,n):
    if s[i-1]=="A" and s[i]=="C":
        lst.append(lst[i-1]+1)
    else:
        lst.append(lst[i-1])

for i in range(q):
    l,r=map(int,input().split())
    print(lst[r-1]-lst[l-1])