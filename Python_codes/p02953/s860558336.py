# Coding by Rute
# C - Build Stairsの解説を始めます。
N = int(input())
H = list(map(int,input().split()))
f = 0 #フラグ関数です。
for i in range(1,N):
  if H[-(i+1)] <= H[-i]:
    #階段の高さが単調非減少かを調べます。
    continue
  else:
    if H[-(i+1)]-H[-i] == 1:
      #そうでない場合、高さが1小さければ、H[-(i+1)]を1小さくすれば良いです。
      #もし高さが2以上小さければ、その時点で単調非減少とすることができないのでフラグ関数に1を加えます。
      H[-(i+1)] -= 1
    else:
      f += 1
      break
if f == 0:
  print("Yes")
else:
  print("No")
#計算量は判定でO(N)かかります。
#以上、C - Build Stairsの解説でした。

