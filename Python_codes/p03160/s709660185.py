from sys import stdin

input=stdin.readline

n=int(input())

cost=[0 for i in range(n)]

s=list(map(int,input().split()))
cost[1]=abs(s[1]-s[0])

for i in range(2,n):
    cost[i]=min(cost[i-1]+abs(s[i]-s[i-1]),cost[i-2]+abs(s[i]-s[i-2]))

print(cost[-1])
