n,p = map(int,input().split())
a = list(map(int,input().split()))

odd = 0
for i in a:
    if i%2:
        odd += 1
even = n-odd

ans = 0

for i in range(0,odd+2,2):
    if i+p > odd:
        break
    for j in range(0,even+1):
        if j > even:
            break
        
        a = 1
        for k in range(i+p):
            a *= (odd-k)
            a /= k+1
    
        b = 1
        for k in range(j):
            b *= (even-k)
            b /= k+1
       
        
        ans += a*b
print(int(ans))

