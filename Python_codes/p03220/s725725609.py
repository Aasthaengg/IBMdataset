n = int(input())
t,a = map(int,input().split())
h = list(map(int,input().split()))

ans = 99999999
ansplace = 0
for cnt, i in enumerate(h):
	if ans > abs(t-i*0.006-a):
		ans = abs(t-i*0.006-a)
		ansplace = cnt
print(ansplace+1)