N=int(input()) 
A=sorted(list(map(int,input().split())))
a=[]
for i in range(N-1):   
    if A[i]==A[i+1]:
        print("NO") 

        break
    elif i==N-2:print("YES")
