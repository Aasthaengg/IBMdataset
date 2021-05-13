N = int(input())
K = int(input())
x_list = list(map(int,input().split()))
ans = 0
for x in x_list:
	A = abs(x)
	babs = K - x
	B = abs(babs)
	mindis = min(A,B)
	ans += (mindis * 2)
print(ans)