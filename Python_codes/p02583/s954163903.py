N = int(input())
L = [int(i) for i in input().split()]
cnt = 0

for a in range(N-2):
  for b in range(a+1, N-1):
    for c in range(b+1, N):
        if L[a] != L[b] and L[b] != L[c] and L[c] != L[a]:
            if L[a]+L[b] > L[c] and L[b]+L[c] > L[a] and L[c]+L[a] > L[b]:
              cnt += 1
print(cnt)