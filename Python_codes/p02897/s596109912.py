from sys import stdin

n = int(stdin.readline().rstrip())

k = int(n/2)
k = n-k
ans = k/n
print(ans)