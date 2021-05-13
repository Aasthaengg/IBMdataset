N,K = map(int,input().split())
A = list(map(int,input().split()))
B = (1+N)*[0]

for a in A:
  B[a]+=1

print(sum(sorted(B)[:-K]))