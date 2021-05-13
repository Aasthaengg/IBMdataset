N,A,B=map(int,input().split())

ans = 0
for i in range(1,N+1):
    s = str(i)
    sum = 0
    for c in s:
        sum += int(c)
    if sum >= A and sum <= B:
        ans += i

print(ans)