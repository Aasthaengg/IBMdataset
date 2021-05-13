r,g,b,n = map(int,input().split())
l = [r,g,b]
l.sort()
count = 0
for i in range(n//l[2]+1):
    for j in range((n-l[2]*i)//l[1]+1):
        if (n-i*l[2]-j*l[1])%l[0] == 0:
            count += 1
print(count)