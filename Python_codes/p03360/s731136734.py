a,b,c = map(int,input().split())
k = int(input())
ans = a+b+c-max(a,b,c)
ans += max(a,b,c)*2**k
print(ans)