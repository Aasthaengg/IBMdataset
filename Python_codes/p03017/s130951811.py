N,A,B,C,D = map(int,input().split())
S = input()

goal = max(C,D)
if '##' in S[A-1:goal]:
  print("No")
  exit()

ok = True
# 追い越す必要がある
if D < C:
  # 間に3マスあきがない or B,Dの間に3マス空きがない
  if ('...' in S[B-1:D]) or ('...' in S[B-2:B+1]) or ('...' in S[D-2:D+1]):
    ok = True
  else:
    ok = False
# 必要がない場合は問題ない

if ok:
  print("Yes")
else:
  print("No")

