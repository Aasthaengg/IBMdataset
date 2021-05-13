N = int(input())
A = list(map(int,input().split()))

DIV = 10**9 + 7

# 0 1 2 3 4 5
# 最初の0で選べるのは3色
# その時点で青・赤・黄とも選択可能だから。

# 0 0 0 
# A (Aとは異なるので)B (A,Bとは異なるので)C
# A,B,Cに3色割り振るので 3 * 2 * 1 = 6

# そこまでにA,B,Cがいくつ出てきたかを記録する。
# 次に選べるもの（複数あればどれでもいい）を選定する
# そのときの候補の数を場合の数に掛け算

ABC = [0] * 3 # A,B,Cが順にいくつ使われたのかの管理

ans = 1
for i in range(N):
  num = A[i]
  first = True
  cnt = 0
  for j in range(len(ABC)):
    if ABC[j] == num:
      cnt += 1
      if first:
        ABC[j] += 1
        first = False
  ans = ((ans % DIV) * cnt)%DIV
  
print(ans)