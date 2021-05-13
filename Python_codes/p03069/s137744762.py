# ....#..#..##.####
# まず、左端の.と右端の#は答えに影響しないので削除する。
# ....#..#..##.####
# #..#..##.
# この結果の文字列が0であればそこで終了
# そうでない場合、
# この結果に対して、黒と白のペアを作って数を数える
# [1,2][1,2][2,1]
# すべて黒にする場合、
# 2 + 2 + 1
# となる
# 白を選ぶ場所を一つずつずらすと、
# 1 + 2 + 1
# 1 + 1 + 1
# 1 + 1 + 2
# となり、1 + 1 + 1が最小値
# これを求める

N=int(input())
S=input()
from collections import deque
q=deque(list(S))
# print(q)

while q[0]==".":
  q.popleft()
  if len(q)==0:
    print(0)
    exit(0)
  
while q[-1]=="#":
  q.pop()
  if len(q)==0:
    print(0)
    exit(0)
  
S="".join(list(q))
pairs=S.replace(".#",". #").split()
# print(pairs)
datas=[[]]*len(pairs)
blackchange=0
for i in range(len(pairs)):
  white=pairs[i].count(".")
  datas[i] = [len(pairs[i])-white,white]
  blackchange+=white

# print(datas)
ans=blackchange
# print(ans)
for i in range(len(datas)):
  blackchange-=(datas[i][1]-datas[i][0])
  if ans > blackchange:
    ans = blackchange
print(ans)