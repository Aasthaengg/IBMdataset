import sys
input = sys.stdin.readline
def MI():
    return map(int, input().split())

n = int(input())
z=[]
w=[]
for i in range(n):
    x,y=MI()
    z.append(x+y)
    w.append(x-y)

print(max(max(z)-min(z), max(w)-min(w)))