a,b,c,k = map(int,input().split())

ans = a-b

if abs(ans) > 10**18:
    print("Unfair")
    exit()

if k%2 == 0:
    print(ans)
else:
    print(-ans)
