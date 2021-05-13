n,l = map(int,input().split())
count = 0
lists = [l+i-1 for i in range(1,n+1)]
x = 2000
for i in range(n):
  if abs(x)>abs(lists[i]):
    x = lists[i]
lists.remove(x)
print(sum(lists))