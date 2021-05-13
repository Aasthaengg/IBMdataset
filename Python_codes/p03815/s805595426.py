x = int(input())
a,b = x//11,x%11
ans = a*2
if b>0:
  ans += 1
if b>6:
  ans += 1
print(ans)

#print(*ans, sep='\n')
