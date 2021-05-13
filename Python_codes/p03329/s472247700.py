N = int(input())
ans = float('inf')
for i in range(N+1):
    j = i
    count = 0
    t=N-i
    while j > 0:
        count += j%6
        j=j//6
    while t > 0:
        count += t%9
        t=t//9
    ans = min(ans,count)
print(ans)
