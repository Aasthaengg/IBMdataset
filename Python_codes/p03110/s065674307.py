n = int(input())
ans = 0
for _ in range(n):
    m,t = input().split()
    m = float(m)
    if t == 'JPY':ans+=m
    else:ans+= m*380000.0
print(ans)
 
