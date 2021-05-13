H, W = list(map(int, input().split()))
A = [[[] for j in range(W)] for i in range(H)]
print("#"*(W+2))
for i in range(H):
  A[i] = input()
  print("#"+A[i]+"#")
print("#"*(W+2))
