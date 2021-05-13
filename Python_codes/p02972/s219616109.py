N=int(input())
binaly=[int(s) for s in input().split()]

boxes=[0 for _ in range(N)]
ans=set()

for i in range(N-1,-1,-1):
  if sum(boxes[i::i+1])%2!=binaly[i]:
    boxes[i]=1
    ans.add(i+1)
print(len(ans))
print(*ans)
