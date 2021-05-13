a,b=map(int,input().split())
List = list(map(int, input().split()))
List.sort(reverse = True)
res = 0
for i in range(b):
  res += List[i]
print(res)