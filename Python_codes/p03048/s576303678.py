r,g,b,n = map(int, input().split())
cnt = 0
for i in range(n+1):
    for j in range(n+1):
        rest = n - i*r - j*g
        if rest >=0 and rest%b==0:
            cnt += 1
print(cnt)