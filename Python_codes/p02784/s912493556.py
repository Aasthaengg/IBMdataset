H,N=map(int,input().split())
List = list(map(int, input().split()))
List.sort(reverse=True)
k = 0
res = "No"
for i in range(N):
  k += List[i]
  if k >= H:
    res = "Yes"
    break
print(res)