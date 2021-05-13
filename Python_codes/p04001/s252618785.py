s=input()
n=len(s)-1
sum=0
for bit in range(1<<n):
	left=0
	right=0
	for i in range(n+1):
		if (bit & (1<<i)):
			left=right
			right=i+1
			sum+=int(s[left:right])
	sum+=int(s[right:n+1])
print(sum)