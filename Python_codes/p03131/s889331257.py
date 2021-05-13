k,a,b = map(int,input().split())

st = max(0, (k-(a-1))//2)

if b-a > 2:
	ans = st*(b-a)+a
	if (k-(a-1)) % 2 == 1:
		ans += 1
	print(ans)
else:
	print(k+1)