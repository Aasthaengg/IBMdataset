A, B, K = map(int, input().split())
Nt = A
Na = B
for i in range(K):
  if i%2==0:
    Nt, Na = Nt//2, Na + (Nt//2)
  else:
    Nt, Na = Nt + (Na//2), Na//2
print(Nt, Na)