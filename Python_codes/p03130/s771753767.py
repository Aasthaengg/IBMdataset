city = [0]*4
for i in range(3):
    a,b = map(int,input().split())
    city[a-1] += 1
    city[b-1] += 1
if city.count(3) == 1:
    print("NO")
else:
    print("YES")