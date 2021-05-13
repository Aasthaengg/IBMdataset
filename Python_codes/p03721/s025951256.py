N,K = map(int,input().split())
arr = sorted([list(map(int,input().split())) for i in range(N)])
total = 0
for i in range(N):
  total+=arr[i][1]
  if total>=K:
    print(arr[i][0])
    exit()