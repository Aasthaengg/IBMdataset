N=int(input())
a=set(4*x+7*y for x in range(200) for y in range(200))
ans="Yes" if N in a else "No"
print(ans)