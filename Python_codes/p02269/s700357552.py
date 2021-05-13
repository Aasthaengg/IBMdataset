dict={}
ans=[]
n=int(input())
for i in range(n):
	a,b=input().split()
	if a=='insert':
		dict.setdefault(b,i)
	elif a=='find':
		if b in dict:
			ans.append('yes')
		else:
			ans.append('no')

for i in ans:
	print(i)
