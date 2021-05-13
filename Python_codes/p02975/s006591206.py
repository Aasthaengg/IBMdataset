import sys
input = sys.stdin.readline
n = int(input())
alist = list(map(int,input().split()))
ans = 0
for i in range(n):
    ans = ans ^ alist[i]
if ans == 0:
    print('Yes')
else:
    print('No')