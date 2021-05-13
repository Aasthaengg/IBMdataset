a, b, c = map(int, input().split())

x = b-a
y = c-b

if x == y:
  ans = 'YES'
else:
  ans = 'NO'
  
print(ans)