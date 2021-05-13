n,T = map(int,input().split())
t = list(map(int,input().split()))
sa = [0]
if n == 1:
    print(T)
    exit()
for i in range(n-1):
    if abs(t[i+1] - t[i]) <= T:
        ans = abs(t[i+1] - t[i])
    elif abs(t[i+1] - t[i]) > T:
        ans = T
    sa.append(ans)
sa.append(T)
print(sum(sa))
        
    
