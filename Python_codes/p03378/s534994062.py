n,m,x = map(int,input().split())
a = [int(x.strip()) for x in input().split()]
toll = [0 for x in range(n+1)]
ans = 0
for i in a:
  toll[i] = 1
ans = min(sum(toll[0:x+1]),sum(toll[x:n+1]))
print(ans)