import sys
sys.setrecursionlimit(10**6)

a1,a2,a3=map(int,input().split())

cost1=abs(a2-a1)+abs(a3-a1)
cost2=abs(a1-a2)+abs(a3-a2)
cost3=abs(a1-a3)+abs(a2-a3)

ans = min(cost1,cost2,cost3)

print(ans)

