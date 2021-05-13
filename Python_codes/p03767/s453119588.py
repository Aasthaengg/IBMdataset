import sys
input = sys.stdin.readline

# A - AtCoder Group Contest
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse = True)
ans = 0

for i in range(1, n * 2, 2):
	ans += a[i]
	
print(ans)