A,B = map(int,input().split())

ans = 0
for x in range(A,B+1):
  x = list(str(x))
  rev_x = x[::-1]
  
  if x == rev_x:
    ans += 1

print(ans)