n,x = map(int,input().split()) 
A= list(map(int,input().split())) 
A.sort()
a_sum=0  
for i in range(n):
    a_sum+= A[i]
    if x<a_sum:
        print(i)
        exit() 

if a_sum== x:
    print(n)
else:
    print(n-1)