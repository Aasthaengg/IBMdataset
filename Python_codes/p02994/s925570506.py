N,L=map(int,input().split())
RES = 0
res = 100
mid = 0
List = []
for i in range(N):
  mid = L+i
  List.append(mid)
  if abs(mid)<abs(res):
    res = mid
for i in range(N):
  if res == List[i]:
    pass
  else:
    RES += List[i]
print(RES)