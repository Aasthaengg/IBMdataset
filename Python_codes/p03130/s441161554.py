from collections import Counter

city = [list(map(int,input().split())) for _ in range(3)]

li = []

for i in range(3):
    for j in range(2):
        li.append(city[i][j])
        
c = Counter(li)

for i in range(1,5):
    if c[i] >= 3:
        print("NO")
        exit()
        
print("YES")