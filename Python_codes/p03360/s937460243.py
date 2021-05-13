mylist=list(map(int,input().split()))
k=int(input())
mylist.sort(reverse=True)
print(mylist[0]*2**k+(sum(mylist)-mylist[0]))