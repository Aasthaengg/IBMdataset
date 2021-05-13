x = int(input())
ans = 0

ans += 2*(x//11)

if 1 <= x%11 < 7:
  ans += 1
elif 7 <= x%11:
  ans += 2
  
print(ans)