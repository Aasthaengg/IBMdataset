def maxValue(a,b,v):
	for i in range(v,-1,-1):
		for j in range(v//a+1): #j:aの個数
			k = i-a*j
			if k%b==0:
				return i

a,b,c,d,e,f = list(map(int, input().split()))

waVa = maxValue(a*100,b*100,f)
suVa = maxValue(c,d,min(f-waVa,waVa*e//100))
maxR = 0

anw = waVa
ans = suVa

while 1:
	waVa = maxValue(a*100,b*100,waVa-1)
	suVa = maxValue(c,d,min(f-waVa,waVa*e//100))
	if waVa == 0:
		break
	if maxR<10000*suVa//(suVa+waVa):
		maxR = 10000*suVa//(suVa+waVa)
		anw = waVa
		ans = suVa

print(anw+ans,ans)