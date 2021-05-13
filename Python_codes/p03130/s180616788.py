a = [0]*5
for i in range(3):
    x,y = map(int,input().split())
    a[x] += 1
    a[y] += 1
    
if max(a) <= 2:
    print("YES")
else:
    print("NO")