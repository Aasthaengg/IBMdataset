a, b = map(int, input().split())

ans = "Impossible"
if a%3==0 or b%3==0 or (a+b)%3==0:
  ans = "Possible"
print(ans)  
