import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n=int(input().rstrip())
c=input().rstrip()
w,r=0,0
for i in c:
    if i=="R":r+=1
    else:w+=1
ans=0
for i in range(r):
    if c[i]=="W":ans+=1
print(ans)