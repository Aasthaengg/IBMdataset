r,g,b,n = map(int,input().split())
ans = 0
cnt = 0
for i in range(n//r+1):
    ans = 0
    for j in range((n-i*r)//g+1):
        ans = i*r+j*g
        a = (n-ans)/b
        if a % 1 == 0:
            cnt +=1
print(cnt)