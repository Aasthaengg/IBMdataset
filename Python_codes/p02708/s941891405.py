n,k = map(int,input().split()) 
ans = 0

# bikkuri_n1 = math.factorial(n+1) % (10**9+7)

# bikkuri_k = math.factorial(k) % (10**9+7)

for i in range(k,n+2):
  
    small = i*(i-1)//2
    big = i*(2*n-i+1)//2
    
    ans += big-small+1
    ans %= (10**9+7)
    
  
    
print(ans)