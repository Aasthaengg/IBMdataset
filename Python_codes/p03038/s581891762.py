n, m =map(int,input().split())
A = list(map(int,input().split()))
BC = [tuple(map(int,input().split()))for i in range(m)]

A.sort()
# 書き換え得点がでかい順に並べる
BC.sort(key= lambda x : -x[1])

i = 0
f=0
for b, c in BC:
    for j in range(b):
      # 見てるとこがはみ出してないかつ、cより小さい
      if i+j<n and A[i+j]<c:
        A[i+j]=c
      else: # もう走査しても意味ないからぶれーく
        break
    i+=b
print(sum(A))