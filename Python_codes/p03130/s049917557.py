li = [0,0,0,0]
for i in range(0,3):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    li[a] += 1
    li[b] += 1
kisuu = 0
for i in li:
    if i % 2 == 1:
        kisuu += 1
if kisuu == 2:
    print("YES")
else:
    print("NO")
