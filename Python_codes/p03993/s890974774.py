n = int(input())

l = list(map(int,input().split()))

ans = 0

for i in range(n):
	if l[l[i]-1]==i+1:
		ans = ans + 1
		#print(i,l[i],l[l[i]-1],i+1)

print(ans//2)
