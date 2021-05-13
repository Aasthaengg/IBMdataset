n = int(input())
A = [int(i) for i in input().split()]
#3 2 2 4 1
B = [int(i) for i in input().split()]
#1 2 2 2 1

ans = 0
for i in range(n):
	ans = max(sum(A[:i+1])+sum(B[i:]),ans)

print(ans)