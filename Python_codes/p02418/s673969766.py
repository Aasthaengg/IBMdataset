s=input()
s+=s
s=list(s)
p=list(input())
def solve(s,p):
	i=0
	while i<len(s):
		if s[i:i+len(p)]==p:
			return("Yes")
		i+=1
	return("No")
print(solve(s,p))