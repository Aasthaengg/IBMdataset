a,b,k=map(int,input().split())
cnt=0
mylist=[]
for i in range(1,10001):
    if a%i==0 and b%i==0:
        mylist.append(i)
print(mylist[-k])