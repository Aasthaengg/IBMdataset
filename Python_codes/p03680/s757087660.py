#1
import sys
n = int(input())
a = []
for i in range(n):
    j = int(input())
    a.append(j)
    
point = a[0]
cnt = 1
for i in range(n):
    if point == 2:
        print(cnt)
        sys.exit()
    point = a[point-1]
    cnt +=1
    
print("-1")