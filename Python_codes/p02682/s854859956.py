a,b,c,k = map(int,input().split())
ans = 0
if k < a:
    ans = k
elif a <= k <= a+b:
    ans = a
elif a+b < k <= a+b+c:
    ans = a-(k-a-b)
print(ans)