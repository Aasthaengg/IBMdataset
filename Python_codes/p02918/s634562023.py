n, k = map(int, input().split())
L=list(input())
cnt=0
if L[0]=='R' and L[1]=='R':
	cnt+=1 

for i in range(1,n-1):
	if L[i]=='R' and L[i+1]=='R':
		cnt+=1
	if L[i]=='L' and L[i-1]=='L':
		cnt+=1

if L[n-1]=='L' and L[n-2]=='L':
	cnt+=1

print(min(cnt+2*k,n-1))