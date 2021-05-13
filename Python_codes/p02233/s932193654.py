list=[1,1]
n=int(input())

t=0
sum=0
if n==0 or n==1:
    print(1)
else:
    for i in range(n):
        list.append(list[i]+list[i+1])
    print(list[n]) 
   
