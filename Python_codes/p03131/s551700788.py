k,a,b=map(int,input().split())
if b-a<=2:
    print(k+1)
else:
    ans = b
    n = k-a-1
    ans += (b-a)*(n//2)
    if n%2:
        ans += 1
    print(ans)