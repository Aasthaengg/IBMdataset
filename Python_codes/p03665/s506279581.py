n,p = map(int,input().split())
A = list(map(int,input().split()))

even = sum([a%2==0 for a in A])
odd = n - even

def nCr(n,r):
  ret = 1
  for i in range(r):
    ret *= n-i
    ret //= i+1  
  return ret
  
ans = 0
add = 2 ** even
for k in range(p,odd+1,2):  
  ans += nCr(odd,k) * add  
  
print(ans)  