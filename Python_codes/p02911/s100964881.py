n,k,q=map(int,input().split())
List=[k-q]*n
for i in range(q):
    a=int(input())
    List[a-1]+=1
for i in List:
    if i>0:
        print("Yes")
    else:
        print("No")