import math
        
def combination(n, k):
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)
            
import collections  
    
n,a,b = map(int,input().split())

t = list(map(int,input().split()))

c = collections.Counter(t)

c = sorted(c.items(), key=lambda x:-x[0])

memo = 0

for k,i in enumerate(c):
    #print(k,i[0],i[1])
    memo += i[1]
    if a<=memo:
        ans = 0
        memo2 = 0
        for j in range(k+1):
            if j != k:
                memo2 += c[j][1]
                ans += c[j][0]*c[j][1]
            else:
                ans += c[j][0]*(a-memo2)
        print(ans/a)
        break
if c[0][1] <= a:  
    print(combination(c[j][1],a-memo2))
else:
    ans1=0
    for l in range(a,min(c[0][1],b)+1):
        ans1 += combination(c[j][1],l)
    print(ans1)