N,A,B,C,D = list(map(int, input().split()))
S = input()

flg = '##' in S[A-1:C] or '##' in S[B-1:D]
if C > D and not flg:
  f,e = max(A-1,B-2),min(D+1,N)

  flg = not '...' in S[f:e]
print("No" if flg else "Yes")