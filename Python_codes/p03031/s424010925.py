N, M = map(int, input().split())
List = [list(map(int, input().split())) for _ in range(M)]
p = list(map(int, input().split()))
num = 0
for i in range(2**N): 
  B = [0 for _ in range(M)] 
  for j in range(N):
    if ((i>>j)&1):
      for k in range(M):
        if j+1 in List[k][1:]:
          B[k] += 1
  for l in range(M):
    if B[l] % 2 != p[l]:
      break
  else:
    num += 1
print(num)