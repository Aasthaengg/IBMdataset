n = int(input())
lst = []
for _ in range(n):
    a,b = map(int,input().split())
    lst.append((a,b,a+b))
lst.sort(key=lambda x:x[2], reverse=True)
x,y = 0,0
for i in range(n):
    if i%2==0:
        x += lst[i][0]
    else:
        y += lst[i][1]
print(x - y)