n,a,b = map(int,input().split())
cnt = 0
for i in range(1,n+1):
    x = sum([int(j) for j in list(str(i))])
    if a <= x <= b:
        cnt += i
print(cnt)