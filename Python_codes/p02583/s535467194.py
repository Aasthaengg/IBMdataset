N = int(input())

L = [int(x) for x in input().split()]

M = []
for a in range(N):
  for b in range(a+1,N):
    for c in range(b+1,N):
      if L[a]+L[b]>L[c] and L[a]+L[c]>L[b] and L[b]+L[c]>L[a] \
      and L[a] != L[b] and L[a] != L[c] and L[b] != L[c]:
        M.append((a,b,c))

print(len(M))