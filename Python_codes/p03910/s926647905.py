n = int(input())

for i in range(1,n+1):
    now = i*(i+1)//2
    if n-now <= 0:
        break

ans = []
for j in range(i,0,-1):
    if n < j:
        if n != 0:
            ans.append(n)
        break
    ans.append(j)
    n -= j
    
for r in ans:
    print(r)