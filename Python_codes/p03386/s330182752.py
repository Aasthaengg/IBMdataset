A,B,K=map(int,input().split())
S=[i for i in range(A,B+1) if i<A+K or i>=B-K+1]
for i in range(len(S)):
  print(S[i])