N,K = map(int,input().split())
A = list(map(int,input().split()))

count =0
first = True
while N >=K:
    if  first ==True:
        count +=1
        N-=K
        first =False
        
    else:
        count+=1
        N-=(K-1)
        
   
    

if N!=0:
    count+=1
print(count)
