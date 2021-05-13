import bisect
n,q=map(int,input().split())
s=list(input())
former_list=[]
latter_list=[]

for i in range(n-1):
    if s[i]=="A" and s[i+1]=="C":
        former_list.append(i+1)
        latter_list.append(i+2)
for j in range(q):
    l,r=map(int,input().split())
    start=bisect.bisect_left(former_list,l)
    end=bisect.bisect_right(latter_list,r)
    print(end-start)