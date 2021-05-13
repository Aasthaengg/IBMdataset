n = int(input())
l = list(map(int,input().split()))

ave=sum(l)/n

for i in range(n):
	l[i]=abs(l[i]-ave)

#print(l)

print(l.index(min(l)))
