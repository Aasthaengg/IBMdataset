# solution

data=int(input())

abc=[list(map(int,input().split())) for _ in [0]*(data-1)]

q,k=map(int,input().split())

array1=[list(map(int,input().split())) for _ in [0]*q]

k-=1

tree=[[] for _ in [0]*data]

dist=[-1]*data

dist[k]=0

[tree[a-1].append([b-1,c]) for a,b,c in abc]

[tree[b-1].append([a-1,c]) for a,b,c in abc]

q=[k]

while(q):
	qq=[]
	for i in q:
		for j,k in tree[i]:
			if dist[j]<0:
				dist[j]=dist[i]+k
				qq.append(j)
	q=qq

for x,y in array1:
	print(dist[x-1]+dist[y-1])
