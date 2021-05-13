n = input()

x = list(map(int,input().split()))

ans = 0

for i in range(1,len(x)-1):
    t = [x[i-1],x[i],x[i+1]]
    t.sort()
    if t[1] == x[i]:
        ans += 1
        
print(ans)