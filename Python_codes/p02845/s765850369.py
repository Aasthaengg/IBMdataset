n = int(input())
a = list(map(int,input().split()))
m = 1000000007
d = [0,0,0]
ans = 1
for i in range(n):
    if d[0] == d[1] == d[2] == a[i]:
        ans *= 3
        d[0] += 1
    elif (d[0] == d[1] or d[1] == d[2]) and a[i] == d[1]:
        ans *= 2
        d[1] += 1
    elif a[i] == d[0]:
        d[0] += 1
    elif a[i] == d[1]:
        d[1] += 1
    elif a[i] == d[2]:
        d[2] += 1
    
    else:
        ans = 0
        break
      
    ans %= m
    d = sorted(d,reverse=True)
print(ans)