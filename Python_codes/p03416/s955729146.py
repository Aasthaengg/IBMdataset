a,b  = map(int, input().split())
cnt = 0
for i in range(a,b+1):
    s = str(i)
    cnt += s==s[::-1]
print(cnt)