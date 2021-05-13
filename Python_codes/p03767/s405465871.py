n = int(input())
a = sorted(map(int,input().split()),reverse=True)
ans = 0
t = (n*3)//3
cnt = 0
i = 1 
while cnt<t:
    cnt += 1
    ans += a[i]
    i += 2
print(ans)