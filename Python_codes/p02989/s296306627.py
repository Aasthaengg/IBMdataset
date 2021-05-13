#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))

n=int(input())
d=input_array()
d.sort()
center=int(n/2)
ans=d[center] - d[center -1] 

print(ans)