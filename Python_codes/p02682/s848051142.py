A,B,C,K = map(int,input().split())

if A>=K:
  max = 1*K
else:
  if B>=(K-A):
    max = 1*A + 0*B
  else:
    max = 1*A + 0*B - 1*(K-A-B)

print(max)