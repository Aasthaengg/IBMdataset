n = int(input())
a = list(map(int, input().split()))

x = max(a)
m = x/2
a.remove(x)
a.sort()
ans = x

for i in a:
    y = abs(i - m)
    if ans >= y:
        ans = y
    else:
        break    
    z = i
      
print(x, z)