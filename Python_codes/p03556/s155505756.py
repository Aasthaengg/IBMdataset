N = int(input())
ans = 0
for i in range(1,N+1):
    if i*i <= N:
        ans = max(ans,i*i)
    else:
        break
print(ans)