n = int(input())
List = list(map(int,input().split()))
ans = 0
temp = 0
for item in List:
  if item > temp:
    ans += item - temp
  temp = item
print(ans)