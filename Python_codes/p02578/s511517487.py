#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))
  
n=int(input())
A=input_array()

front=0 # 1つ前の人の身長
ans=0 # 踏み台のたかさの合計
for a in A:
	if a < front:
		ans+=front-a
	else:
		front=a

print(ans)