n=int(input())
l=[]
a=10**9
for i in range(n):
  l.append([int(i) for i in input().split()])
ll=sorted(l)
print(ll[-1][0]+ll[-1][1])