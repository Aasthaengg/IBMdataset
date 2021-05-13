n=int(input())
a=list(map(int,input().split()))
if n==0 and a[0]==1:
	print(1)
elif n==0:
	print(-1)
elif a[0]!=0:
	print(-1)
else:
	ruisekiwa = [0 for _ in range(n+1)]
	ruisekiwa[n] = a[n]
	for i in range(n)[::-1]:
		ruisekiwa[i] = a[i] + ruisekiwa[i+1]
	cnt=1
	ans=1
	for i in range(1,n+1):
		target = a[i]
		if cnt*2 - target <= 0 and i != n:
			print(-1)
			exit()
		elif i == n:
			if cnt * 2 - target < 0:
				print(-1)
				exit()
			else:
				ans += target
		else:
			if cnt*2 < ruisekiwa[i]:
				ans += cnt*2
				cnt = cnt*2-a[i]
			else:
				ans += ruisekiwa[i]
				cnt = ruisekiwa[i]
	print(ans)