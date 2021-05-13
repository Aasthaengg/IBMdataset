#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))

a=input_array()

ALL=sum(a)
MAX=max(a)

print(ALL-MAX)