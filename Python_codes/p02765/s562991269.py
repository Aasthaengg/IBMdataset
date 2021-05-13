a,b = map(int, input().split())
if a < 10:
  ans = b + 100*(10 - a)
else:
  ans = b
print(ans)
	
