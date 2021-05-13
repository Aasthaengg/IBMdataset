x, k, d =map(int, input().split()) 
ans = 0; x = abs(x)

if int(x/d) >= k:
	ans = x-d*k
else:
	k = k - int(x/d)
	x = abs(x - d*int(x/d))
	if (k - int(x/d)) % 2 == 1:
		ans = abs(x - d)
	else:
		ans = x


print(ans)
