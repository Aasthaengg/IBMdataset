n,k = map(int,input().split())
H = list(map(int,input().split()))
b = 0
for h in H:
	if(k <= h):
		b +=1   
print(b)
