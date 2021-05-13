N=int(input())
a_list = list(map(int,input().split()))
ans = 0
min = a_list[0]
for i in range(1,N):
  if min > a_list[i]:
    ans += min-a_list[i]
  else:
    min = a_list[i]
print(ans)