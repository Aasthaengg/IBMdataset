n,x = list(map(int, input().split()))
lst = [0]+list(map(int, input().split()))
ans = 0

for i in range(n):
    if lst[i]+lst[i+1]>x:
        ans+=(lst[i]+lst[i+1]-x)
        lst[i+1]-=(lst[i]+lst[i+1]-x)
print(ans)
