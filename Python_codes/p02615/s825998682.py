n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
ans = a[0]
ans += sum(a[1:((n-1)//2+1)])*2
if n % 2:
    ans -= a[n//2]
print(ans)