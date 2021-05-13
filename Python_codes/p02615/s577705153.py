import heapq

#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))

n=int(input())
A=input_array()
sortA=sorted(A,reverse=True) #降順にソート

ans=0
q=[]
heapq.heappush(q,-sortA[0])

for i in range(1,n):
	tmp=heapq.heappop(q)
	tmp*=-1
	ans+=tmp
	heapq.heappush(q,-sortA[i])
	heapq.heappush(q,-sortA[i])
print(ans)