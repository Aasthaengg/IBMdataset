import sys
S = list(input())
S.insert(0,"X")

#文字列の奇数番目をチェック
for i in range(1,len(S),2):
  if S[i] == "L":
    print("No")
    sys.exit()
#文字列の偶数番目をチェック
for j in range(2,len(S),2):
  if S[j] == "R":
    print("No")
    sys.exit()
print("Yes")