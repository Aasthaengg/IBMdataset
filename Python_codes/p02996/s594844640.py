n=int(input())
tab = []
for i in range(n):
	a,b = map(int,input().split())
	tab+=[[a,b]]
	
def cle(x):
	return x[1]
tab.sort(key = cle)

ans = "Yes"

temps = 0
for a,b in tab:
	temps+=a
	if temps>b: ans = "No"
	
print(ans)
