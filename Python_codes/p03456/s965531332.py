a,b=map(str,input().split())
ab=int(a+b)

ans="No"
for i in range(1,350):
  if i**2==ab:
    ans="Yes"
    break

print(ans)