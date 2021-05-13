n,k = [int(i) for i in input().split()]
td = [[int(i) for i in input().split()] for _ in range(n)]

###dが大きい順にソート
td.sort(key = lambda x: x[1],reverse=True)

###各tでdが最大のものを格納
fix_eated_d=[]
###各tでdが最大でないものを格納。tの種類を増やす際の削除候補
change_eated_d=[]

eated_t = set()
d_point = 0

###まずdを最大化
for t,d in td[:k]:
  
  ###すでにtが選ばれているなら最大のdではないのでchangeへ
  if t in eated_t:
    change_eated_d.append(d)
    
  ###まだtが選ばれていないなら最大のdだからfixへ
  else:
    fix_eated_d.append(d)
    eated_t.add(t)
    
  d_point += d
  
point = len(eated_t)**2 + d_point

###tの種類を増やす
for t,d in td[k:]:
  ###削除候補がなくなれば終了
  if not change_eated_d:
    break
  
  ###すでにtが選ばれているならskip
  if t in eated_t:
    continue
    
  ###まだtが選ばれていないなら追加、change中dが最小のものを削除
  eated_t.add(t)
  d_point += d - change_eated_d.pop()
  point = max(point, len(eated_t)**2 + d_point)
  
print(point)


