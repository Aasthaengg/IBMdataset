r,g,b,n = map(int,input().split())
cnt = 0
l = [r,g,b]
l.sort()
r = l[2]
g = l[1]
b = l[0]

for i in range(n//r + 1):
    for j in range((n-r*i)//g + 1):
        if (n-r*i-g*j)%b == 0:
            cnt += 1
print(cnt)
