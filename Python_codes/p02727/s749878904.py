x,y,a,b,c = map(int,input().split())
p = sorted(list(map(int,input().split())),reverse=True)
q = sorted(list(map(int,input().split())),reverse=True)
r = sorted(list(map(int,input().split())),reverse=True)
result = sum(p[0:x]) + sum(q[0:y])
red = x-1
green = y-1
colorless = 0
#print(p,q,r)
while colorless < c:
	#print(red,green,colorless)
	if red >= 0 and green >= 0:
		if p[red] < q[green]:
			if r[colorless] > p[red]:
				result -= p[red]
				result += r[colorless]
				colorless += 1
				red -= 1
			else:
				break
		else:
			if r[colorless] > q[green]:
				result -= q[green]
				result += r[colorless]
				colorless += 1
				green -= 1
			else:
				break
	elif red >= 0:
		if r[colorless] > p[red]:
			result -= p[red]
			result += r[colorless]
			colorless += 1
			red -= 1
		else:
			break
	elif green >= 0:
		if r[colorless] > q[green]:
			result -= q[green]
			result += r[colorless]
			colorless += 1
			green -= 1
		else:
			break
print(result)