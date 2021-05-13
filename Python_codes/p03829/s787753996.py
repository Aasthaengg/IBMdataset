n,a,b = map(int,input().split())
x = list(map(int,input().split()))
xdif = [x2-x1 for x1,x2 in zip(x,x[1:])]
ans = sum(dx*a if dx*a <b  else b for dx in xdif)
print(ans)