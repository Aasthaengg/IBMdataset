import sys
input = sys.stdin.readline
n = int(input())
l = []
for i in range(n):
    a,b = map(int,input().split())
    l.append((b,a))
l.sort()
t = 0
for i in range(n):
    t += l[i][1]
    if t > l[i][0]:
        print('No')
        exit()
print('Yes')