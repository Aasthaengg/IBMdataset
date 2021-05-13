n=int(input())
a=[int(j) for j in input().split()]
b=[int(j) for j in input().split()]
tmp=0
if tmp<0:
    print("No")
    exit()
for i,j in zip(a,b):
   if i>j:
       tmp+=j-i
   elif i<j:
       tmp+=(j-i)//2
if tmp>=0:
    print("Yes")
else:
    print("No")