N,i=map(int,input().split())
list1=[x+1 for x in range(0,1000)]
list2=[y for y in range(1,N+1)]
if N in list1 and i in list2:
     x=(N-i)+1 
     print(x)