a,b=input().split()
ab=int(a+b)
ans=0
for i in range(350):
	if ab**(1/2)==i:
	    print("Yes")
	    ans+=1
	    quit()
if ans==0:
  print("No")