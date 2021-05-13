n=int(input())
a,b=map(int, input().split())
l=list(map(int, input().split()))
ul=[]
ml=[]
ol=[]
sorted(l)
for i in range(n):
	if l[i]<=a:
		ul.append(l[i])
	elif (a+1)<=l[i]<=b:
		ml.append(l[i])
	elif l[i]>=(b+1):
		ol.append(l[i])
print(min(len(ul),len(ml),len(ol)))