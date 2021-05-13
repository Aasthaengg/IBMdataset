# 全ての集合のペアに、共通の値を一つずつ入れる
# 集合がA,B,Cの3個の場合、AとBを結ぶ数値は1,AとBを結ぶ数値は2、CとAは3、というようにペアごとに
# 異なる数値を割り振る
# A  B  C
# 1  1
# 2     2
#    3  3
# これにより、
# (1,2),(1,3),(2,3)となる。
# 集合の数が4個の場合は同様に
# A B C D
# 1 1
# 2   2  
# 3     3
#   4 4
#   5   5
#     6 6
# (1,2,3)(1,4,5)(2,4,6)(3,5,6)
# xC2で表現できるNの場合はこの構成が可能。(4C2 = 6なので、N = 6のとき可能)
# その際x個の集合ができる（上の場合4個）
# N = 10 ** 5のため、x * (x - 1) // 2 = たかだか10**5の数を2つずつ集合に割り振っていけば構成可能
# なおN = 1のときは(1)(1)が答え

N = int(input())
if N == 1:
  print("Yes")
  print(2)
  print(1,1)
  print(1,1)
  exit(0)
  
X = -1
for x in range(2,449):
  if (x * (x - 1) % 2) == 0 and (x * (x - 1) // 2) == N:
    X = x
    break
else:
  print("No")
  exit(0)
  
# X個の集合ができる
num = 1
ans = [set() for i in range(X)]
for i in range(len(ans)-1):
  for j in range(i+1,len(ans)):
    ans[i].add(num)
    ans[j].add(num)
    num += 1
    
print("Yes")
print(X)
for a in ans:
  print(len(a),*a)
