N=int(input())
mylist=list(map(int,input().split()))
point=0

mylist.sort(reverse=True)

#print(mylist)

for i in range(N):
    point+=mylist[2*i+1]
    
print(point)