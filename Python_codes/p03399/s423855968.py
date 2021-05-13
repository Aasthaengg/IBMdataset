l= sorted([int(input()) for _ in range(2)])
m=sorted([int(input()) for _ in range(2)])

ans= min(x+y for x,y in zip(l,m))
print(ans)