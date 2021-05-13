l = [0,0,0,0]
for i in range(3):
    a,b = map(int,input().split())
    l[a-1] += 1
    l[b-1] += 1

if (max(l) == 3)or(min(l) == 0):
    print("NO")
else:
    print("YES")

