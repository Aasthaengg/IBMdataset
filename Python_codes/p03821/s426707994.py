import sys
def input(): return sys.stdin.readline().strip()
n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
c=0
for i in range(n):
    l[n-1-i][0]+=c
    c+=-l[n-1-i][0]%l[n-1-i][1]
print(c)