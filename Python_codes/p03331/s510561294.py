n = int(input())
ans = 10000000000

for i in range(n//2):
    x = i+1
    y = str(n-x)
    x = str(x)
    z = 0

    for c in x:
        z += int(c)
    for c in y:
        z += int(c)
    
    if z < ans:
        ans = z

print(ans)