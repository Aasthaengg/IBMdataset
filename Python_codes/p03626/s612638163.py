N=input()
S1=raw_input()
S2=raw_input()

mod=1000000007

str=""
i=0
while i<N:
	if S1[i]==S2[i]:
		str+="t"
		i+=1
	else:
		str+="y"
		i+=2


l=len(str)

ans=1
if str[0]=="t": ans*=3
else: ans*=6

for i in range(l-1):
	now=str[i]
	next=str[i+1]
	if now=="t" and next=="y":
		ans*=2
	elif now=="t" and next=="t":
		ans*=2
	elif  now=="y" and next=="y":
		ans*=3
	elif  now=="y" and next=="t":
		ans*=1
	ans%=mod

print ans
