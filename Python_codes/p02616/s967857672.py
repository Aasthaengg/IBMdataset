def func(A, n, k): 
    A.sort() 
    product = 1

    if (A[n - 1] == 0 and (k & 1)): 
        return 0

    if (A[n - 1] <= 0 and (k & 1)) : 
        for i in range(n - 1, n - k - 1, -1): 
            product = (product*A[i])%mod
        return product 

    i = 0
    j = n - 1
    if (k & 1): 
        product = (product*A[j])%mod 
        j-= 1
        k-=1

    k >>= 1
  
    for itr in range( k) : 
        left_product = A[i] * A[i + 1] 
 
        right_product = A[j] * A[j - 1] 
  
        if (left_product > right_product) : 
            product = (product*(left_product%mod))%mod
            i += 2
          
        else : 
            product = (product*(right_product%mod))%mod
            j -= 2
  
    return product 


n,k=map(int,input().split())
arr=list(map(int,input().split()))
global mod
mod=1000000007
ans=func(arr,n,k)
print(ans%mod)