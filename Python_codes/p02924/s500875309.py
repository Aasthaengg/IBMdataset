import sys
input = sys.stdin.readline

# D - ModSum
n = int(input())

if (n-1) % 2 == 0:
	ans = n * (n-1)//2
else:
	ans = (n-1) * n//2

print(ans)