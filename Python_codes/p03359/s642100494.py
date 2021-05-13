(a, b) = (int(tok) for tok in input().split())
res = a - 1
  
if b >= a:
	res += 1

print(res)