x,y=map(int,input().split())
lis=[1,3,1,2,1,2,1,1,2,1,2,1]
print(["Yes","No","No","Yes","x","No","x","x","x","Yes"][lis[x-1]*lis[y-1]-1])