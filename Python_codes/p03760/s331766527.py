 
o=input()
e=input()
cnt=0
i , j = 0 , 0
a = len(o)
b = len(e)
ans = ''
while i<a or j<b:
	if cnt%2==0:
 		ans = ans+(o[i])
 		i = i+1
 		cnt = cnt+1
	else:
		ans =ans+(e[j])
		j =j+1
		cnt =cnt+1
while i<a:
	ans = ans+(o[i])
	i = i+1
print(ans)