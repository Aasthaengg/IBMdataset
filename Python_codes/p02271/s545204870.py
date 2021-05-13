from itertools import combinations as comb

n=int(input())
lst=list(map(int,input().split()))

numlst=[]
for i in range(1,n+1):
    for x in comb(lst,i):
        y=sum(x)
        if not y in numlst:
            numlst.append(y)

q=int(input())
lst2=list(map(int,input().split()))
for x in lst2:
    if x in numlst : print("yes")
    else : print("no")
