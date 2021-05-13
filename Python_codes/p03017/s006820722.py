N, A, B,C,D = map(int,input().split())
S = list(input())

a = A-1
b = B-1
c = C-1
d = D-1

ans = 1

for i_a in range(a,C):
  #2連続の##がa~Cにないことを確認
  if S[i_a] == "#":
    if S[i_a+1] == "#":
      ans =0

for i_b in range(b,D):
  #2連続の##がb~Dにないことを確認
  if S[i_b] == "#":
    if S[i_b+1] == "#":
      ans =0

if D < C:
  ans = 0
  for i in range(b,D):
    #3連続があるなら1
    if S[i-1] == ".":
      if S[i] == ".":
        if S[i+1] == ".":
          ans = 1

if ans ==1:
  print("Yes")
else:
  print("No")
