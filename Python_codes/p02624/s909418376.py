n=int(input())
ans=0
for i in range(n):
    
    m=n//(i+1)
    
    ans += (i+1) *m*(m+1)/2
    
print(int(ans))
