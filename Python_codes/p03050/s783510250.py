N=int(input())
def div(n):
    low,high= [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            low.append(i)
            if i != n // i:
                high.append(n//i)
        i += 1
    return low+high[::-1]
S=div(N)
ans=0
S=S[1:]
for i in S:
   if i==0:
      continue
   if N%(i-1)==N//(i-1):
      ans+=i-1
print(ans)