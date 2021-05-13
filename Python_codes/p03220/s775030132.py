N=int(input())
T,A=map(int,input().split())
mylist=list(map(int,input().split()))
mymin=10**6
index=0

for i in range(N):
  if(mymin>abs(A-(T-0.006*mylist[i]))):
    mymin=abs(A-(T-0.006*mylist[i]))
    index=i
print(index+1)
