N=int(input())
a=[int(t.strip()) for t in input().split()]
cnt=0
p=[[0 for i in range(2)] for j in range(2*N)]

if min(a) >= 0:#正数のみ
	for i in range(N-1):
		if a[i] > a[i+1]:
			#print(i+1,i+2)
			p[cnt][0]=i+1
			p[cnt][1]=i+2
			
			a[i+1] += a[i]
			cnt+=1
elif max(a)<0:#非自然数のみ
	for i in reversed(range(1,N)):
		if a[i] < a[i-1]:
			a[i-1] += a[i]
			#print(i+1,i)
			p[cnt][0]=i+1
			p[cnt][1]=i
			cnt+=1
else:#負も正も混同
	if max(a) > min(a)*-1:
		tmp=max(a)
		ind = a.index(max(a))
		for i in range(N):
			a[i] +=tmp
			#print(ind+1,i+1)
			p[cnt][0]=ind+1
			p[cnt][1]=i+1
			cnt+=1
		for i in range(N-1):
			if a[i] > a[i+1]:
				#print(i+1,i+2)
				p[cnt][0]=i+1
				p[cnt][1]=i+2
				cnt+=1
				a[i+1] += a[i]
	else:
		tmp=min(a)
		ind = a.index(min(a))
		for i in range(N):
			a[i] +=tmp
			#print(ind+1,i+1)
			p[cnt][0]=ind+1
			p[cnt][1]=i+1
			cnt+=1
		for i in reversed(range(1,N)):
			if a[i] < a[i-1]:
				a[i-1] += a[i]
				#print(i+1,i)
				p[cnt][0]=i+1
				p[cnt][1]=i
				cnt+=1

print(cnt)
for i in range(cnt):
	print(p[i][0],p[i][1])
#print(a)