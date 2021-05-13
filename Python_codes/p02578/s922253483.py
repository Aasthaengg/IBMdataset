from sys import stdin
input = stdin.readline

n = int(input())
a = list(map(int,input().split()))
ma = -1
res = 0
for i in a:
    res += max(ma - i,0)
    ma = max(ma,i)
print(res)
