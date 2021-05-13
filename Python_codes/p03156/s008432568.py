N=int(input())
A,B=map(int,input().split())
P=list(map(int,input().split()))
listA=[]
listB=[]
listC=[]
for i in P:
    if i<=A:
        listA.append(i)
    elif A+1<=i<=B:
        listB.append(i)
    else:
        listC.append(i)
print(min(len(listA),len(listB),len(listC)))