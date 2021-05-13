n = int(input())
ans = 0

for i in range(n-1):
    if n%(i+1)==0:
        ans += n//(i+1)-1
    else:
        ans += n//(i+1)

print(ans)
