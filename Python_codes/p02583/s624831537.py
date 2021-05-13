import itertools
import sys
N = int(input())
if N < 3:
  print(0)
  sys.exit()
 
#辺を取得してint型に変換
hen_list = input().split()
for i in range(len(hen_list)):
    hen_list[i] = int(hen_list[i])
 
#組み合わせ
count = 0
for tri in itertools.combinations(hen_list, 3):
    sort_tri = sorted(tri)
    if sort_tri[0] + sort_tri[1] > sort_tri[2]:
        if tri[0] != tri[1] and tri[0] != tri[2] and tri[1] != tri[2]:
            #print(sort_tri)
            count += 1
print(count)