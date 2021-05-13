N=int(input())
h=list(map(int,input().split()))
Answer=h[0]
 
for i in range(N-1):
    if h[i]<=h[i+1]:
        m=h[i+1]-h[i]
        Answer=Answer+m
        
print(Answer)