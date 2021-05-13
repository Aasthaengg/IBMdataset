n,m=map(int,input().split())
count = 0
result=[[[i,j] for i in range(m)] for j in range(n)]
result.pop(0)
for i in result:
  i.pop()
  count += len(i)
print(count)